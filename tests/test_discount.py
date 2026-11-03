import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("DVD", cost=100))

    def test_twenty_percent_discount_returns_eighty(self):
        self.assertAlmostEqual(self.cart.discount(20), 80)

    def test_percent_above_one_hundred_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.cart.discount(150)


if __name__ == "__main__":
    unittest.main()
