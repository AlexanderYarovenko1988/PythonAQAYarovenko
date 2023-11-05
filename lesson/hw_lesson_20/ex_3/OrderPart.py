from Dish import Dish


class OrderPart:
    def __init__(self, id: int, name: str, dish: Dish):
        self.id = id
        self.name = name
        self.dish = dish

    def getPrice(self):
        return self.dish.getPrice()

    def __str__(self):
        return f"{self.name}{self.dish.getName()}. Ціна: {self.getPrice()} гривень"

