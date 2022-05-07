from unittest import TestCase
from unittest.mock import MagicMock, patch
from src.config import Config
from src.repository import Repository
from src.domain import Position
from src.lambdas.check_off_route import check_off_route


module_path = check_off_route.__module__


class TestLambdaCheckOffRoute(TestCase):
    def setUp(self):
        patch.object(Config, 'LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE', '50').start()

        self.point_mock = MagicMock()
        self.route_mock = MagicMock()
        self.distance_mock = 100

        def exec():
            with patch.object(Repository, 'get_route', return_value=self.route_mock) as get_route_mock, \
                    patch(f'{module_path}.project_point', return_value=self.point_mock) as proj_point_mock, \
                    patch(f'{module_path}.get_point_to_line_distance', return_value=self.distance_mock) as point_to_line_mock:

                self.off_route = check_off_route(Position(-7.118443, -34.879287, 10, 5))
                self.get_route_mock = get_route_mock
                self.proj_point_mock = proj_point_mock
                self.point_to_line_mock = point_to_line_mock

        self.exec_fn = exec
        self.exec_fn()

    def test__position_is_off_route(self):
        self.assertTrue(self.off_route)

    def test__get_route_should_be_called_with_route_id(self):
        self.assertEqual(self.get_route_mock.call_args[0][0], 5)

    def test__project_point_should_be_called_with_correct_coords(self):
        self.assertEqual(self.proj_point_mock.call_args[1]['lat'], -7.118443)
        self.assertEqual(self.proj_point_mock.call_args[1]['lng'], -34.879287)

    def test__point_to_line_distance_should_be_called_with_correct_params(self):
        self.assertEqual(self.point_to_line_mock.call_args[0][0], self.point_mock)
        self.assertEqual(self.point_to_line_mock.call_args[0][1], self.route_mock)

    def test__position_is_not_off_route(self):
        self.distance_mock = 40 # less than the max tolerated distance
        self.exec_fn()
        self.assertFalse(self.off_route)
