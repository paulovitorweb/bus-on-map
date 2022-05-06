import psycopg2
from redis import Redis
from src.config import Config


class RedisClient:
    _conn = None

    @classmethod
    def get_instance(cls):
        if not cls._conn:
            cls._conn = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)
        return cls._conn


class PostgresDatabase:
    _conn = None

    @classmethod
    def get_instance(cls):
        if not cls._conn:
            cls._conn = psycopg2.connect(
                "host='{}' port='{}' dbname='{}' user='{}' password='{}'".format(
                    Config.POSTGRES_DB_HOST,
                    Config.POSTGRES_DB_PORT,
                    Config.POSTGRES_DB_NAME,
                    Config.POSTGRES_DB_USER,
                    Config.POSTGRES_DB_PASS,
                )
            )
        return cls._conn
