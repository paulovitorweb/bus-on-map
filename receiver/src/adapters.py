from src.domain import Position
from kafka import KafkaProducer


producer: KafkaProducer = None


def init_stream():
    """Start stream with kafka integration"""
    global producer
    producer = KafkaProducer(
        bootstrap_servers='localhost:29092', 
        value_serializer=lambda v: v.encode('utf-8')
    )


class Config:
    """Centralize kafka settings"""
    POSITIONS_TOPIC = 'positions'


def stream(position: Position):
    """Put the position in stream"""
    producer.send(Config.POSITIONS_TOPIC, position.to_json())
