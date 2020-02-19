import unittest
import json

from src.app import app


class TestAppRoutes(unittest.TestCase):
    def test_health(self):
        self.app = app.test_client()

        actual = self.app.get('/health')

        data = json.loads(actual.get_data(as_text=True))

        self.assertEqual(actual.status_code, 200)
        self.assertEqual(data['response'], 'App is healthy!')
