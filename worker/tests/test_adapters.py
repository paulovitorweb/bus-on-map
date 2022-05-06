from unittest import TestCase
from unittest.mock import patch
from src.adapters import RedisClient
from src.config import Config


class TestRedisClient(TestCase):
    def setUp(self):
        self._module = RedisClient.__module__

        patch.object(Config, 'REDIS_HOST', 'host').start()
        patch.object(Config, 'REDIS_PORT', '6378').start()

    def test__get_instance_should_return_the_same_instance(self):
        with patch(f'{self._module}.Redis'):
            instance = RedisClient().get_instance()
            instance2 = RedisClient().get_instance()

            self.assertIs(instance, instance2)
    
    def test__get_instance_should_call_redis_with_correct_params(self):
        with patch(f'{self._module}.Redis') as redis:
            RedisClient().get_instance()

            redis.assert_called_once_with(host='host', port='6378', decode_responses=True)
