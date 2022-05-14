from dataclasses import FrozenInstanceError
from uuid import UUID
from unittest import TestCase
from src.domain import Position


class TestPositionModel(TestCase):
    def setUp(self):
        self.position = Position(lat=-7.118443, lng=-34.879287, vehicle_id=1, route_id=10)

    def test__should_create_an_instance(self):
        self.assertEqual(self.position.lat, -7.118443)
        self.assertEqual(self.position.lng, -34.879287)
        self.assertEqual(self.position.vehicle_id, 1)
        self.assertEqual(self.position.route_id, 10)
        self.assertIsInstance(self.position.correlation_key, UUID)

    def test__instance_should_be_frozen(self):
        def change_position():
            self.position.lat = -7.2

        self.assertRaises(FrozenInstanceError, change_position)

    def test__should_raise_an_exception_if_any_input_data_is_missing(self):
        self.assertRaises(TypeError, lambda: Position(lat=-7.118443, lng=-34.879287))

    def test__to_json_method_should_return_a_string(self):
        expected = '"lat": -7.118443, "lng": -34.879287, "vehicle_id": 1, "route_id": 10, "correlation_key": '
        self.assertIn(expected, self.position.to_json())
