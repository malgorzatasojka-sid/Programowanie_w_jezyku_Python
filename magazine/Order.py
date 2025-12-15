from magazine import utils


class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return utils.format_price(self.product.price * self.quantity)
