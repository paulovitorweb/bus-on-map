from redis import Redis
from src.config import Config


class RedisClient:
    _conn = None

    @classmethod
    def get_instance(cls):
        if not cls._conn:
            cls._conn = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)
        return cls._conn
