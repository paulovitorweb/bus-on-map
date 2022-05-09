from typing import Optional
from src.domain import Position, Alert


def check_bus_exceeded_capacity(position: Position) -> Optional[Alert]:
    """Checks whether the vehicle has exceeded the passenger carrying capacity"""
    return 