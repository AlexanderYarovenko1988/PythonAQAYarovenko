from Dish import Dish

class Drink(Dish):
    def __init__(self, name: str, price: float, type: str = "cold"):
        super().__init__(name, price)
        self.type = type

    def getType(self):
        return self.type
