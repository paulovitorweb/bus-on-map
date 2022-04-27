class SSE {
  static eventType = {
    POSITION: 'position'
  }

  constructor(response) {
    this._response = response
  }

  init() {
    const headers = {
      'Content-Type': 'text/event-stream',
      'Connection': 'keep-alive',
      'Cache-Control': 'no-cache'
    }
    this._response.writeHead(200, headers)
  }

  sendMessage(event, data) {
    this._response.write(`event: ${event}\n`)
    this._response.write(`data: ${JSON.stringify(data)}\n\n`)
  }
}

module.exports = SSE