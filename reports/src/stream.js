const { Kafka } = require('kafkajs')
const SSE = require('./sse')
const Clients = require('./clients')
const { 
    KAFKA_CLIENT_ID, 
    KAFKA_BROKER, 
    KAFKA_GROUP_ID, 
    KAFKA_POSITIONS_TOPIC 
} = require('./config')

const kafka = new Kafka({
  clientId: KAFKA_CLIENT_ID,
  brokers: [KAFKA_BROKER]
})

const consumer = kafka.consumer({groupId: KAFKA_GROUP_ID})
const clients = new Clients().getInstance()

async function eachMessage({ topic, partition, message }) {
    let data = JSON.parse(message.value.toString())
    clients.sendToAll(SSE.eventType.POSITION, data)
}

async function startStream() {
    await consumer.connect()
    await consumer.subscribe({ topic: KAFKA_POSITIONS_TOPIC })
    await consumer.run({eachMessage})
}

module.exports = { startStream }