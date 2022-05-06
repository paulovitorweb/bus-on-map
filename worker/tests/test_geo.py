from unittest import TestCase
from shapely import wkt
from src.geo import project_point, get_point_to_line_distance


class TestGeo(TestCase):
    def setUp(self):
        self.coords = -7.165245, -34.873884
        wkt_line = 'LINESTRING (293275.005443 9207464.025653001, 293188.729407 9207544.85919)'
        self.linestring = wkt.loads(wkt_line)

    def test__project_point_should_return_correct_coords(self):
        utm_point = project_point(*self.coords)

        self.assertEqual(293065.26482166443, utm_point.x)
        self.assertEqual(9207561.610154282, utm_point.y)

    def test__point_to_line_distance_should_return_distance_in_meters(self):
        utm_point = project_point(*self.coords)
        distance = get_point_to_line_distance(utm_point, self.linestring)

        self.assertEqual(124.5957408440002, distance)
