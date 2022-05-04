from unittest import TestCase
from json.decoder import JSONDecodeError
from dataclasses import FrozenInstanceError
from src.domain import Position


class TestNewPosition(TestCase):
    def setUp(self) -> None:
        str_position ='{"lat": -7.118443, "lng": -34.879287, "vehicle_id": 1, "route_id": 10}'
        self.position = Position.from_json(str_position)

    def test__new_position_should_have_latitude(self):
        self.assertEqual(self.position.lat, -7.118443)

    def test__new_position_should_have_longitude(self):
        self.assertEqual(self.position.lng, -34.879287)

    def test__new_position_should_have_vehicle_id(self):
        self.assertEqual(self.position.vehicle_id, 1)

    def test__new_position_should_have_route_id(self):
        self.assertEqual(self.position.route_id, 10)

    def test__new_position_instance_should_be_frozen(self):
        def change_position():
            self.position.lat = -7.2
        self.assertRaises(FrozenInstanceError, change_position)

    def test__new_position_should_fail_due_to_invalid_input_json(self):
        self.assertRaises(JSONDecodeError, lambda: Position.from_json('a invalid input'))

    def test__new_position_should_fail_due_to_missing_input_data(self):
        self.assertRaises(TypeError, lambda: Position.from_json('{"lat": -7.118443, "lng": -34.879287}'))
