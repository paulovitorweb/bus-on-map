from typing import Optional
from src.domain import Position, Alert


def check_bus_bunching(position: Position) -> Optional[Alert]:
    """Checks if buses on the same line are are bunching"""
    return