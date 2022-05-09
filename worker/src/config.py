import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    APP_ID = None
    POSITIONS_TOPIC = None
    ALERTS_TOPIC = None
    REDIS_HOST = None
    REDIS_PORT = None
    KAFKA_BROKER = None
    POSTGRES_DB_HOST = None
    POSTGRES_DB_PORT = None
    POSTGRES_DB_NAME = None
    POSTGRES_DB_USER = None
    POSTGRES_DB_PASS = None
    LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE = None
    LAMBDA_OFF_ROUTE_INTERVAL_IN_SECONDS = None
    CACHE_ROUTE_EXPIRATION_IN_SECONDS = None


def load_config():
    Config.APP_ID = os.environ.get('APP_ID', 'worker_app')
    Config.POSITIONS_TOPIC = os.environ.get('POSITIONS_TOPIC', 'positions3')
    Config.ALERTS_TOPIC = os.environ.get('ALERTS_TOPIC', 'alerts')
    Config.REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    Config.REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
    Config.KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'localhost:29092')
    Config.POSTGRES_DB_HOST = os.environ.get('POSTGRES_DB_HOST', 'localhost')
    Config.POSTGRES_DB_PORT = os.environ.get('POSTGRES_DB_PORT', '5432')
    Config.POSTGRES_DB_NAME = os.environ.get('POSTGRES_DB_NAME', 'postgres')
    Config.POSTGRES_DB_USER = os.environ.get('POSTGRES_DB_USER', 'postgres')
    Config.POSTGRES_DB_PASS = os.environ.get('POSTGRES_DB_PASS', 'postgres')
    Config.LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE =  \
        os.environ.get('LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE', '50')
    Config.LAMBDA_OFF_ROUTE_INTERVAL_IN_SECONDS =  \
        os.environ.get('LAMBDA_OFF_ROUTE_INTERVAL_IN_SECONDS', '60')
    Config.CACHE_ROUTE_EXPIRATION_IN_SECONDS =  \
        os.environ.get('CACHE_ROUTE_EXPIRATION_IN_SECONDS', '60')


load_config()