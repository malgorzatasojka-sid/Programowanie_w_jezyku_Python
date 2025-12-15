from magazine import utils


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} - {utils.format_price(self.price)}"
