// configure minimal network settings and key storage
const config = {
  nodeUrl: 'https://rpc.testnet.near.org',
  deps: {
    keyStore: new nearApi.keyStores.BrowserLocalStorageKeyStore()
  }
};

// open a connection to the NEAR platform
(async function() {
  window.near = await nearApi.connect(config);

  // ---------------------------------------------------------------------------
  // here you have access to `near-api-js` and a valid connection object `near`
  // ---------------------------------------------------------------------------

})(window)
