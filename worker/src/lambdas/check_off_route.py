from src.logger import Logger
from src.config import Config
from src.geo import project_point, get_point_to_line_distance
from src.repository import Repository
from src.domain import Position


def check_off_route(position: Position) -> bool:
    """Checks if the vehicle is off route"""
    route = Repository().get_route(position.route_id)
    point = project_point(lat=position.lat, lng=position.lng)
    distance = get_point_to_line_distance(point, route)

    is_off_route = distance > int(Config.LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE)

    if not is_off_route:
        return False

    logger = Logger().get_instance()
    logger.warning(f'The bus {position.vehicle_id} is off route {route.id}')

    return True
