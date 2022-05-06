from unittest import TestCase
from json.decoder import JSONDecodeError
from dataclasses import FrozenInstanceError
from shapely.geometry.linestring import LineString
from src.domain import Position, Route


class TestDomainPosition(TestCase):
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


class TestDomainRoute(TestCase):
    def setUp(self) -> None:
        wktext = 'LINESTRING(293275.05 9207464.02,293188.72 9207544.85)'
        self.route = Route(1, '204', 'CRISTO REDENTOR', wktext)

    def test__new_route_should_have_id(self):
        self.assertEqual(self.route.id, 1)

    def test__new_route_should_have_code(self):
        self.assertEqual(self.route.code, '204')
    
    def test__new_route_should_have_name(self):
        self.assertEqual(self.route.name, 'CRISTO REDENTOR')
    
    def test__new_route_should_have_geom_as_wkt(self):
        self.assertEqual(self.route.geom, 'LINESTRING(293275.05 9207464.02,293188.72 9207544.85)')

    def test__new_route_should_have_linestring(self):
        self.assertIsInstance(self.route.linestring, LineString)

    def test__new_route_instance_should_be_frozen(self):
        def change_route():
            self.route.code = '203'
        self.assertRaises(FrozenInstanceError, change_route)

    def test__new_route_should_fail_due_to_missing_input_data(self):
        self.assertRaises(TypeError, lambda: Route(1, '204', 'CRISTO'))
