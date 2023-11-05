from Dish import Dish


class Risotto(Dish):
    def __init__(self, name: str, price: float, type: str = "hot"):
        super().__init__(name, price)
        self.type = type

    def getType(self):
        return self.type

class Pasta(Dish):
    def __init__(self, name: str, price: float, type: str = "hot"):
        super().__init__(name, price)
        self.type = type

    def getType(self):
        return self.type

class Pizza(Dish):
    def __init__(self, name: str, price: float, type: str = "hot"):
        super().__init__(name, price)
        self.type = type

    def getType(self):
        return self.type