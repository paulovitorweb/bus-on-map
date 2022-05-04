from unittest import TestCase
from unittest.mock import patch
from src.adapters import RedisClient


class TestRedisClient(TestCase):
    def setUp(self):
        self._module = RedisClient.__module__

        class ConfigMock:
            REDIS_HOST = 'host'
            REDIS_PORT = '6378'

        patch(f'{self._module}.Config', ConfigMock).start()

    def test__get_instance_should_return_the_same_instance(self):
        with patch(f'{self._module}.Redis'):
            instance = RedisClient().get_instance()
            instance2 = RedisClient().get_instance()

            self.assertIs(instance, instance2)
    
    def test__get_instance_should_call_redis_with_correct_params(self):
        with patch(f'{self._module}.Redis') as redis:
            RedisClient().get_instance()

            redis.assert_called_once_with(host='host', port='6378', decode_responses=True)
