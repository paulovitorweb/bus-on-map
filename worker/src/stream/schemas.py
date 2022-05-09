import faust
from src.domain import AlertType


class PositionRecord(faust.Record):
    lat: float
    lng: float
    vehicle_id: int
    route_id: int
    correlation_key: str


class AlertRecord(faust.Record):
    type: AlertType
    correlation_key: str
    extra: dict