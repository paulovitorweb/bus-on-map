require('dotenv/config.js')
const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const { handler } = require('./handlers')
const { startStream } = require('./stream')
const { API_PORT } = require('./config')

const app = express()

app.use(cors())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))

app.get('/events', handler)

app.listen(API_PORT, async () => await startStream())