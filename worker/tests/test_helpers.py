from unittest import TestCase
from unittest.mock import patch
from src.helpers.cache import get_route
from src.adapters import RedisClient
from src.repository import Repository
from src.domain import Route


class TestCacheHelper(TestCase):
    def setUp(self) -> None:
        pass

    def test__get_route_should_return_route_from_cache(self):
        route_cache_mock = (
            '{"id": 1, "code": "0204", "name": "CRISTO REDENTOR", '
            '"geom": "LINESTRING()"}'
        )
        with patch.object(RedisClient, 'get_instance') as redis_mock, \
                patch.object(Repository, 'get_route') as get_route_repo_mock:
            redis_mock.return_value.get.return_value = route_cache_mock
            route = get_route(1)

            self.assertIsInstance(route, Route)
            redis_mock.return_value.set.assert_not_called()
            get_route_repo_mock.assert_not_called()
    
    def test__get_route_should_return_route_from_database(self):
        route_mock = Route(1, '01', 'ANY', 'LINESTRING()')
        with patch.object(RedisClient, 'get_instance') as redis_mock, \
                patch.object(Repository, 'get_route', return_value=route_mock) as get_route_repo_mock:
            redis_mock.return_value.get.return_value = None
            route = get_route(1)

            self.assertIsInstance(route, Route)
            redis_mock.return_value.set.assert_called()
            get_route_repo_mock.assert_called_once_with(1)
