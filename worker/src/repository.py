from psycopg2 import Error
from src.domain import Route
from src.adapters import PostgresDatabase
from src.logger import Logger


class Repository:
    """Read-only repository that abstracts read to PostgreSQL database"""
    def get_route(self, route_id: int) -> Route:
        query = (
            'SELECT id, code, name, ST_AsText(geom) geom '
            'FROM core_route '
            'WHERE id = %s'
        )
        row = self._run_query_and_fetch_one(query, (route_id,))
        return Route(*row)

    def _run_query_and_fetch_one(self, query: str, args: tuple) -> tuple:
        db = PostgresDatabase().get_instance()
        cursor = None
        try:
            cursor = db.cursor()
            cursor.execute(query, args)
            result = cursor.fetchone()
        except (Exception, Error) as e:
            Logger().get_instance().error(f'Database error: {e}')
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            db.close()

        return result
        
