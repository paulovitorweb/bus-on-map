# Bus-on-map reports

API responsible for reporting events to the monitoring page.

Events sent by the server (Server-sent events) are used to communicate with the client, maintaining stream connections with a Nodejs server using express.

## Development

Add an `.env` file with the content:

```
KAFKA_BROKER=localhost:29092
KAFKA_CLIENT_ID=reports-api
KAFKA_GROUP_ID=reports-api
API_PORT=3000
KAFKA_POSITIONS_TOPIC=positions
```

With kafka broker running, run the server:

```
npm start
```