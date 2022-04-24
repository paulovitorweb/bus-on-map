from unittest import TestCase
from fastapi.testclient import TestClient
from src.api import app


class TestApi(TestCase):
    def setUp(self):
        self.client = TestClient(app)
    
    def test__api_should_receive_position(self):
        payload = {'lat': -7.118443, 'lng': -34.879287, 'vehicle_id': 1, 'route_id': 10}
        response = self.client.post('/positions/', json=payload)
        self.assertEqual(response.status_code, 200)

    def test__api_should_return_an_422_http_status_if_payload_is_invalid(self):
        payload = {'lat': -7.118443, 'lng': -34.879287}
        response = self.client.post('/positions/', json=payload)
        self.assertEqual(response.status_code, 422)
