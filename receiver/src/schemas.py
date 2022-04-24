from pydantic import BaseModel


class PositionSchema(BaseModel):
    """Schema to validate the payload"""
    lat: float
    lng: float
    vehicle_id: int
    route_id: int
