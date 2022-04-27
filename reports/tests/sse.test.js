const SSE = require('../src/sse')

class MockResponse {
  writeHead (status, headers) {
    // pass
  }

  write (text) {
    // pass
  }
}

describe('SSE class', () => {
  const response = new MockResponse()
  const sse = new SSE(response)

  it('it should init SSE', () => {
    jest.spyOn(response, 'writeHead')
    const expectedHeaders = {
      'Content-Type': 'text/event-stream',
      Connection: 'keep-alive',
      'Cache-Control': 'no-cache'
    }
    expect(sse.init()).toBeUndefined()
    expect(response.writeHead).toHaveBeenCalledWith(200, expect.objectContaining(expectedHeaders))
  })

  it('it should send message', () => {
    jest.spyOn(response, 'write')
    sse.sendMessage(SSE.eventType.POSITION, { lat: -7.11, lng: -34.87 })
    expect(response.write).toHaveBeenNthCalledWith(1, 'event: position\n')
    expect(response.write).toHaveBeenNthCalledWith(2, 'data: {\"lat\":-7.11,\"lng\":-34.87}\n\n')
  })
})
