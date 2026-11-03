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

    def test_sort_by_title(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("The Lion King", cost=19.95)
        dvd2 = DigitalVideoDisc("Star Wars", cost=24.95)
        dvd3 = DigitalVideoDisc("Aladdin", cost=18.99)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.add_dvd(dvd3)

        cart.sort_by_title()
        self.assertEqual([dvd.title for dvd in cart.items], ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_title_same_title_higher_cost_first(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Aladdin", cost=15.00)
        dvd2 = DigitalVideoDisc("Aladdin", cost=25.00)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)

        cart.sort_by_title()
        self.assertEqual(cart.items, [dvd2, dvd1])

    def test_sort_by_cost(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Aladdin", cost=18.99)
        dvd2 = DigitalVideoDisc("Star Wars", cost=24.95)
        dvd3 = DigitalVideoDisc("The Lion King", cost=19.95)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.add_dvd(dvd3)

        cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in cart.items], [24.95, 19.95, 18.99])

    def test_sort_by_cost_same_cost_alphabetical_title(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Star Wars", cost=20.00)
        dvd2 = DigitalVideoDisc("Aladdin", cost=20.00)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)

        cart.sort_by_cost()
        self.assertEqual(cart.items, [dvd2, dvd1])

    def test_sort_empty_cart(self):
        cart = Cart()
        cart.sort_by_title()
        self.assertEqual(cart.items, [])
        cart.sort_by_cost()
        self.assertEqual(cart.items, [])

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
