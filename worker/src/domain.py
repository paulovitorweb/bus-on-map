import json
from dataclasses import dataclass


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