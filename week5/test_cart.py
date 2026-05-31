import unittest

from cart import Cart


class TestCart(unittest.TestCase):
    def test_add_item(self):
        cart = Cart()
        cart.add_item({"name": "Pizza", "price": 10})
        self.assertEqual(len(cart.items), 1)

    def test_remove_item(self):
        cart = Cart()
        cart.add_item({"name": "Pizza", "price": 10})
        cart.remove_item({"name": "Pizza", "price": 10})
        self.assertEqual(len(cart.items), 0)

    def test_cart_total(self):
        cart = Cart()
        cart.add_item({"name": "Pizza", "price": 10})
        self.assertEqual(cart.p(cart.items), 10)


if __name__ == "__main__":
    unittest.main()
