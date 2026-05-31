import unittest
from unittest.mock import Mock

from data_service import DataService


class TestDataService(unittest.TestCase):
    def test_get_restaurants_returns_api_payload(self):
        api_client = Mock()
        api_client.get.return_value = [{"id": 1, "name": "Luigi's"}]
        service = DataService(api_client)
        self.assertEqual(service.get_restaurants(), [{"id": 1, "name": "Luigi's"}])

    def test_get_restaurants_calls_correct_endpoint(self):
        api_client = Mock()
        api_client.get.return_value = []
        service = DataService(api_client)
        service.get_restaurants()
        api_client.get.assert_called_once_with("/restaurants")

    def test_get_restaurant_by_id(self):
        api_client = Mock()
        api_client.get.return_value = {"id": 1, "name": "Luigi's"}
        service = DataService(api_client)
        self.assertEqual(service.get_restaurant(1), {"id": 1, "name": "Luigi's"})


if __name__ == "__main__":
    unittest.main()
