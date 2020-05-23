import datetime
import hashlib
import json
from flask import Flask, jsonify

#Building a Blockchain

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0',WaterType="NA",FlowRate=0,IndustryID="NA")

    def create_block(self, proof, previous_hash,WaterType,FlowRate,IndustryID):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'message':f"{IndustryID}#{WaterType}#{FlowRate}",
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

#Mining our Blockchain

#Test Variables
WaterType=["Dirty Water","Fresh Water"]
FlowRate=[1000,2000,3000,4000]
IndustryID=["INS23ASW","IND23ASW","INS44ASW","INS24ASW","INS23LKW"]
#WasteWater Implementation
from random import randint as ri
# Creating a Web App
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    wT=WaterType[ri(0,len(WaterType)-1)]
    fR=FlowRate[ri(0,len(FlowRate)-1)]
    iID=IndustryID[ri(0,len(IndustryID)-1)]
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash,wT,fR,iID)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    try:print(response["chain"][1]["message"])
    except:print("No blocks mined yet")
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Shivam, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200
app.run(host = '0.0.0.0', port = 5000)
