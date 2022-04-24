import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """Position model"""
    lat: float
    lng: float
    vehicle_id: int
    route_id: int

    def to_json(self) -> str:
        """Transform a position object into a json string
        
        Used to send to kafka"""
        return json.dumps(self.__dict__)
