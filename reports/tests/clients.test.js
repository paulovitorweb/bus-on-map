const Clients = require('../src/clients')

class mockSseResponse {
    sendMessage(event, data) {
        // pass
    }
}

describe('Clients singleton', () => {
    jest.useFakeTimers('modern').setSystemTime(new Date(2022, 4, 26, 22))
    const response = new mockSseResponse()
    const clients = new Clients()
    let clientId

    it('it should init clients with empty list', () => {
        expect(clients.getInstance()._clients).toEqual([])
    })

    it('it should add new client', () => {
        clientId = clients.getInstance().addNewClient(response)
        expect(clients.getInstance()._clients.length).toEqual(1)
    })

    it('the id of the new customer added should be equal to the date of now', () => {
        expect(clientId).toEqual(1653613200000)
    })

    it('it should send message to all clients', () => {
        jest.spyOn(response, 'sendMessage')
        clients.getInstance().sendToAll('position', 'data')
        expect(response.sendMessage).toHaveBeenCalledTimes(1)
        expect(response.sendMessage).toHaveBeenCalledWith('position', 'data')
    })

    it('it should remove a client', () => {
        clients.getInstance().removeClient(1653613200000)
        expect(clients.getInstance()._clients.length).toEqual(0)
    })
})