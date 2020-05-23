const config = {
  nodeUrl: 'https://rpc.testnet.near.org',
  deps: {
    keyStore: new nearApi.keyStores.UnencryptedFileSystemKeyStore()
  }
};

// open a connection to the NEAR platform
(async function() {
  global.near = await nearApi.connect(config);

  // ---------------------------------------------------------------------------
  // here you have access to `near-api-js` and a valid connection object `near`
  // ---------------------------------------------------------------------------

})(global)
