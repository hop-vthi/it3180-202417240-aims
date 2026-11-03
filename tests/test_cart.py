import contextlib
import io
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

    def test_print_cart_default_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=100.0))
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            cart.print_cart()
            printed = output.getvalue()
        self.assertIn("Total cost: 100.00 $", printed)
        self.assertIn("Total cost after discount: 100.00 $", printed)

    def test_print_cart_with_discount_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=100.0))
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            cart.print_cart(20)
            printed = output.getvalue()
        self.assertIn("Total cost: 100.00 $", printed)
        self.assertIn("Total cost after discount: 80.00 $", printed)


if __name__ == "__main__":
    unittest.main()
