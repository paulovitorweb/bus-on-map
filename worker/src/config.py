import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    REDIS_HOST = None
    REDIS_PORT = None


def load_config():
    Config.REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    Config.REDIS_PORT = os.environ.get('REDIS_PORT', '6379')


load_config()
