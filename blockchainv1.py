import datetime
import hashlib
import json
from flask import Flask, jsonify, render_template
from flask_cors import CORS

#Building a Blockchain

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0',wTT="NA",CreditScore=0,FlowRate=0,industryID="NA")

    def create_block(self, proof, previous_hash,wTT,CreditScore,FlowRate,industryID):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'message':f"{industryID}#{wTT}#{FlowRate}#{CreditScore}",
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
#FlowRate=[1000,2000,3000,4000]
IndustryID=["INS23ASW","IND23ASW","INS44ASW","INS24ASW","INS23LKW"]
#WasteWater Implementation
import cv2
from WaterClassifier import WaterType,FlowRateClassifier
import numpy as np
cam=cv2.VideoCapture("demovideo.mp4") #Change this to cv2.VideoCapture(0) for using real-time camera feed
x=203
y=97
w=39
h=36
_,frame=cam.read()
Background=cv2.resize(frame,(640,480)).copy()
skipFrames=140 #These are initial frames that need to be skipped before the actual flow starts
#Note that in real time video capture this won't be required as water is flowing and that will be captured by camera frame in continious basis
for i in range(skipFrames):
    _,frame=cam.read()
framerates=[]
labels=['Fresh water','Waste Water']
watertypes=[]
#Frames=[]
count=0
def ProcessFrame(Frame):
    Frame=cv2.resize(Frame,(640,480))
    wTT=labels[labels.index(WaterType(Frame,x,y,w,h))]
    fRR=FlowRateClassifier(Frame,Background,x,y,w,h)
    print(f"wtt={wTT},and frame rate= {fRR}")
    CreditScore=(fRR*0.01)+(10**(not(labels.index(WaterType(Frame,x,y,w,h))))*0.09)-0.2 #Credit earned
    waterLabel=labels[not(WaterType(Frame,x,y,w,h))] #Water Type Detected
    print(f"Water Label={wTT} and CreditScore={CreditScore}% and FlowRate={fRR} sq pixels/s")
    return(wTT,CreditScore,fRR)

#from random import randint as ri
# Creating a Web App
app = Flask(__name__)
CORS(app)
# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block
#Random variables
wT='Clean Water'
fR=0
iID="ASC6368"
#@app.route('/', methods = ['GET'])
'''@app.route('/home')
def home():
    return render_template('index.html')'''
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    _,frame=cam.read()
    wTT,CreditScore,FlowRate=ProcessFrame(frame)
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash,wTT,CreditScore,FlowRate,iID)
    response = {'message': 'Data sent to the server!',
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
if __name__=="__main__":
    app.run(host = '0.0.0.0', port = 5000,debug=True)
