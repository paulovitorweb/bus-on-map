from unittest import TestCase
from unittest.mock import patch
from kafka import KafkaProducer
from src.domain import Position
from src.adapters import Config, stream


class TestStream(TestCase):
    def setUp(self):
        self.position = Position(lat=-7.118443, lng=-34.879287, vehicle_id=1, route_id=10)
        self.json = self.position.to_json()

    def test__should_call_the_function_that_sends_to_kafka(self):
        with patch.object(KafkaProducer, 'send') as send_to_kafka, \
                patch.object(Config, 'POSITIONS_TOPIC', 'positions'): 
            stream(self.position)
            topic, message = send_to_kafka.call_args[0]
            self.assertEqual(topic, 'positions')
            self.assertEqual(message, self.json)
