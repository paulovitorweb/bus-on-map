class Clients {
  constructor () {
    this._clients = []
  }

  sendToAll (event, data) {
    this._clients.forEach(({ response }) => response.sendMessage(event, data))
  }

  addNewClient (response) {
    const clientId = Date.now()
    const newClient = {
      id: clientId,
      response
    }
    this._clients.push(newClient)
    return clientId
  }

  removeClient (clientId) {
    this._clients = this._clients.filter(client => client.id !== clientId)
  }
}

class ClientsSingleton {
  constructor () {
    if (!ClientsSingleton._instance) {
      ClientsSingleton._instance = new Clients()
    }
  }

  getInstance () {
    return ClientsSingleton._instance
  }
}

module.exports = ClientsSingleton
