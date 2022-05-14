from typing import Optional
from src.logger import Logger
from src.config import Config
from src.geo import project_point, get_point_to_line_distance
from src.domain import Position, Alert, AlertType
from src.helpers import cache


def check_off_route(position: Position) -> Optional[Alert]:
    """Checks if the vehicle is off route"""
    route = cache.get_route(position.route_id)
    point = project_point(lat=position.lat, lng=position.lng)
    distance = get_point_to_line_distance(point, route.linestring)

    is_off_route = distance > int(Config.LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE)

    if not is_off_route:
        return

    distance = round(distance)

    logger = Logger().get_instance()
    logger.warning(
        f'The bus <{position.vehicle_id}> is off route <{route}> - '
        f'Distance: {distance} meters - '
        f'Correlation key: {position.correlation_key}'
    )

    return Alert(
        type=AlertType.OFF_ROUTE.value,
        correlation_key=position.correlation_key,
        extra=dict(
            bus=position.vehicle_id,
            route=route.id,
            distance=distance
        )
    )
