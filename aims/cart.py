MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Discount percent must be between 0 and 100")
        return self.total_cost() * (1 - percent / 100)

    def print_cart(self, percent):
        print("***********************CART***********************")
        print("Ordered Items:")
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print(f"Total cost after discount: {self.discount(percent):.2f} $")
        print("**************************************************")
