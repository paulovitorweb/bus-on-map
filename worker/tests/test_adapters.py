from unittest import TestCase
from unittest.mock import patch
from src.adapters import RedisClient
from src.config import Config


class TestRedisClient(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._module = RedisClient.__module__

        cls.mock_redis_host = patch.object(Config, 'REDIS_HOST', 'host')
        cls.mock_redis_port = patch.object(Config, 'REDIS_PORT', '6378')

        cls.mock_redis_host.start()
        cls.mock_redis_port.start()

    def test__get_instance_should_return_the_same_instance(self):
        with patch(f'{self._module}.Redis'):
            instance = RedisClient().get_instance()
            instance2 = RedisClient().get_instance()

            self.assertIs(instance, instance2)
    
    def test__get_instance_should_call_redis_with_correct_params(self):
        with patch(f'{self._module}.Redis') as redis:
            RedisClient().get_instance()

            redis.assert_called_once_with(host='host', port='6378', decode_responses=True)

    @classmethod
    def tearDownClass(cls):
        RedisClient._conn = None
        cls.mock_redis_host.stop()
        cls.mock_redis_port.stop()
