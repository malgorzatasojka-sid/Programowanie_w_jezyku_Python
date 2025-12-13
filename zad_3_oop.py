class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House at {self.address}, "
            f"area: {self.area} m², "
            f"rooms: {self.rooms}, "
            f"plot: {self.plot} m², "
            f"price: {self.price}"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat at {self.address}, "
            f"area: {self.area} m², "
            f"rooms: {self.rooms}, "
            f"floor: {self.floor}, "
            f"price: {self.price}"
        )


house1 = House(
    area=120,
    rooms=5,
    price=750000,
    address="Katowice, Bankowa 10",
    plot=400
)

flat1 = Flat(
    area=60,
    rooms=3,
    price=420000,
    address="Bytom, Sobieskiego 5",
    floor=3
)

print(house1)
print(flat1)
