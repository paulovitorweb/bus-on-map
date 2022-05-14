import json
from uuid import uuid4, UUID
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Position:
    """Position model"""

    lat: float
    lng: float
    vehicle_id: int
    route_id: int
    correlation_key: UUID = field(default_factory=uuid4)

    def to_json(self) -> str:
        """Transform a position object into a json string

        Used to send to kafka"""
        value = self.__dict__
        value['correlation_key'] = str(value['correlation_key'])
        return json.dumps(self.__dict__)
