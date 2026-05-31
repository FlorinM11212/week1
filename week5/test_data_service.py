import unittest
from unittest.mock import Mock

from data_service import DataService


class TestDataService(unittest.TestCase):
    def setUp(self):
        # Once and Only Once: the mock API client and the service under test
        # are built here, not re-created inside every test method.
        self.api_client = Mock()
        self.service = DataService(self.api_client)

    def test_get_restaurants_returns_api_payload(self):
        self.api_client.get.return_value = [{"id": 1, "name": "Luigi's"}]
        self.assertEqual(self.service.get_restaurants(), [{"id": 1, "name": "Luigi's"}])

    def test_get_restaurants_calls_correct_endpoint(self):
        self.api_client.get.return_value = []
        self.service.get_restaurants()
        self.api_client.get.assert_called_once_with("/restaurants")

    def test_get_restaurant_by_id(self):
        self.api_client.get.return_value = {"id": 1, "name": "Luigi's"}
        self.assertEqual(self.service.get_restaurant(1), {"id": 1, "name": "Luigi's"})


if __name__ == "__main__":
    unittest.main()
