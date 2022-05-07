import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    REDIS_HOST = None
    REDIS_PORT = None
    POSTGRES_DB_HOST = None
    POSTGRES_DB_PORT = None
    POSTGRES_DB_NAME = None
    POSTGRES_DB_USER = None
    POSTGRES_DB_PASS = None
    LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE = None


def load_config():
    Config.REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    Config.REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
    Config.POSTGRES_DB_HOST = os.environ.get('POSTGRES_DB_HOST', 'localhost')
    Config.POSTGRES_DB_PORT = os.environ.get('POSTGRES_DB_PORT', '5432')
    Config.POSTGRES_DB_NAME = os.environ.get('POSTGRES_DB_NAME', 'postgres')
    Config.POSTGRES_DB_USER = os.environ.get('POSTGRES_DB_USER', 'postgres')
    Config.POSTGRES_DB_PASS = os.environ.get('POSTGRES_DB_PASS', 'postgres')
    Config.LAMBDA_MAX_DISTANCE_TOLERATED_OUT_OF_ROUTE =  \
        os.environ.get('LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE', '50')


load_config()