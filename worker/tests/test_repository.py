from unittest import TestCase
from unittest.mock import patch
from src.domain import Route
from src.adapters import PostgresDatabase as Database
from src.repository import Repository


class TestRepository(TestCase):
    def setUp(self) -> None:
        self.repo = Repository()

    def test__repository_should_fail_when_connecting(self):
        with patch.object(Database, 'get_instance', side_effect=ConnectionError):
            self.assertRaises(ConnectionError, lambda: self.repo.get_route(1))

    def test__repository_should_handle_exception_when_get_cursor(self):
        with patch.object(Database, 'get_instance') as mock_db:
            mock_db.return_value.cursor.side_effect = ConnectionError

            self.assertRaises(ConnectionError, lambda: self.repo.get_route(1))
            mock_db.return_value.close.assert_called()

    def test__repository_should_handle_exception_when_execute_query(self):
        with patch.object(Database, 'get_instance') as mock_db:
            cursor = mock_db.return_value.cursor.return_value
            cursor.execute.side_effect = ConnectionError

            self.assertRaises(ConnectionError, lambda: self.repo.get_route(1))
            cursor.close.assert_called()
            mock_db.return_value.close.assert_called()

    def test__repository_should_get_route(self):
        res_mock = (1, '204', 'CRISTO REDENTOR', 'LINESTRING(293275.05 9207464.02,293188.72 9207544.85)')

        with patch.object(Database, 'get_instance') as mock_db:
            cursor = mock_db.return_value.cursor.return_value
            cursor.fetchone.return_value = res_mock

            route = self.repo.get_route(1)

            self.assertIsInstance(route, Route)
            self.assertEqual(route.id, 1)
            self.assertEqual(route.code, '204')
            self.assertEqual(route.name, 'CRISTO REDENTOR')
            self.assertEqual(route.geom, 'LINESTRING(293275.05 9207464.02,293188.72 9207544.85)')

            cursor.close.assert_called()
            mock_db.return_value.close.assert_called()
            
