import json
from src.config import Config
from src.logger import Logger
from src.adapters import RedisClient
from src.repository import Repository
from src.domain import Route


_ROUTE_CACHE_PREFIX = 'route_'


def get_route(route_id):
    """Function to get route using cache.
    If the cache not exists, get from database.
    """
    route_cache_key = f'{_ROUTE_CACHE_PREFIX}{route_id}'
    cache = RedisClient().get_instance()
    cached_route = cache.get(route_cache_key)

    if cached_route:
        print(cached_route)
        route = json.loads(cached_route)
        return Route(**route)

    db_route = Repository().get_route(route_id)
    cache.set(
        route_cache_key, 
        json.dumps(db_route.__dict__), 
        ex=int(Config.CACHE_ROUTE_EXPIRATION_IN_SECONDS)
    )

    Logger().get_instance().info(f'Cache set for route {route_id}')

    return db_route
