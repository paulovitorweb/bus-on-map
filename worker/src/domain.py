import json
from typing import NewType
from dataclasses import dataclass
from shapely.geometry.linestring import LineString
from src.geo import load_linestring



Wkt = NewType('Wkt', str)


@dataclass(frozen=True)
class Position:
    """Position model"""

    lat: float
    lng: float
    vehicle_id: int
    route_id: int

    @staticmethod
    def from_json(json_string: str) -> 'Position':
        """creates a position object from a json string"""
        position = json.loads(json_string)
        return Position(**position)


@dataclass(frozen=True)
class Route:
    """Route model"""

    id: int
    code: str
    name: str
    geom: Wkt

    @property
    def linestring(self) -> LineString:
        return load_linestring(self.geom)
