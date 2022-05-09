import json
from typing import NewType
from dataclasses import dataclass
from enum import Enum
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
    correlation_key: str

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

    def __str__(self):
        return f'{self.code} - {self.name}'


class AlertType(Enum):
    OFF_ROUTE = 'OFF_ROUTE'
    BUNCHING = 'BUNCHING'
    PASSENGER_CAPACITY_EXCEEDED = 'PASSENGER_CAPACITY_EXCEEDED'


@dataclass(frozen=True)
class Alert:
    """Alert model"""

    type: AlertType
    correlation_key: str
    extra: dict
