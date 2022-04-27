const SSE = require('./sse')
const Clients = require('./clients')

const clients = new Clients().getInstance()

function handler (request, response, next) {
  const sse = new SSE(response)

  sse.init()

  const clientId = clients.addNewClient(sse)

  request.on('close', () => {
    console.log(`${clientId} Connection closed`)
    clients.removeClient(clientId)
  })
}

module.exports = {
  handler
}
