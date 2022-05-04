import pyproj
from shapely.geometry.point import Point
from shapely.geometry.linestring import LineString
from shapely.ops import transform


def project_point(lat: float, lng: float) -> Point:
    """Project point from WSG84 to metric system"""
    wgs_point = Point(lng, lat)

    wgs_crs = pyproj.CRS('EPSG:4326')
    utm_crs = pyproj.CRS('EPSG:31985')

    project = pyproj.Transformer.from_crs(wgs_crs, utm_crs, always_xy=True).transform

    utm_point = transform(project, wgs_point)

    return utm_point


def get_point_to_line_distance(point: Point, line: LineString) -> float:
    """Returns the distance from the point to the line, in meters. 
    Assume the point and line are both in the same metric coordinate system.
    """
    return line.distance(point)