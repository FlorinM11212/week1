import unittest

from cart import Cart


class TestCart(unittest.TestCase):
    def setUp(self):
        # Once and Only Once: the shared arrangement lives here instead of
        # being repeated at the top of every test method.
        self.cart = Cart()
        self.cart.add_item({"name": "Pizza", "price": 10})

    def test_add_item(self):
        self.assertEqual(len(self.cart.items), 1)

    def test_remove_item(self):
        self.cart.remove_item({"name": "Pizza", "price": 10})
        self.assertEqual(len(self.cart.items), 0)

    def test_cart_total(self):
        self.assertEqual(self.cart.calculate_total(), 10)

    def test_log_counter_tracks_operations(self):
        # setUp already added one item (1 operation); removing makes it 2.
        self.cart.remove_item({"name": "Pizza", "price": 10})
        self.assertEqual(self.cart.operation_count(), 2)


if __name__ == "__main__":
    unittest.main()
