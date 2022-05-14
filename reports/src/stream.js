const { Kafka } = require('kafkajs')
const SSE = require('./sse')
const Clients = require('./clients')
const {
  KAFKA_CLIENT_ID,
  KAFKA_BROKER,
  KAFKA_GROUP_ID,
  KAFKA_POSITIONS_TOPIC,
  KAFKA_ALERTS_TOPIC
} = require('./config')

const kafka = new Kafka({
  clientId: KAFKA_CLIENT_ID,
  brokers: [KAFKA_BROKER]
})

const consumer = kafka.consumer({ groupId: KAFKA_GROUP_ID })
const clients = new Clients().getInstance()

const eventMap = {}
eventMap[KAFKA_POSITIONS_TOPIC] = SSE.eventType.POSITION
eventMap[KAFKA_ALERTS_TOPIC] = SSE.eventType.ALERT

async function eachMessage ({ topic, partition, message }) {
  const data = JSON.parse(message.value.toString())
  clients.sendToAll(eventMap[topic], data)
}

async function startStream () {
  await consumer.connect()
  await consumer.subscribe({ topic: KAFKA_POSITIONS_TOPIC })
  await consumer.subscribe({ topic: KAFKA_ALERTS_TOPIC })
  await consumer.run({ eachMessage })
}

module.exports = { startStream }
