class Dish:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
