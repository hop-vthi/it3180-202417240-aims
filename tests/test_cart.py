import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_twenty_discs_then_reject_twenty_first(self):
        cart = Cart()

        for number in range(1, 21):
            with self.subTest(disc=number):
                self.assertIs(cart.add_dvd(DigitalVideoDisc(f"DVD {number}")), True)

        self.assertEqual(len(cart.items), 20)

        extra_disc = DigitalVideoDisc("DVD 21")
        self.assertIs(cart.add_dvd(extra_disc), False)
        self.assertEqual(len(cart.items), 20)
        self.assertNotIn(extra_disc, cart.items)


if __name__ == "__main__":
    unittest.main()
