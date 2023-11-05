from datetime import datetime
from Dish import Dish
from OrderPart import OrderPart
import csv

class Order:
    def __init__(self, time, orderParts=[]):
        self.time = time.replace(second=0, microsecond=0)  # Округлити час до хвилин
        self.orderParts = orderParts

    def __str__(self):
        order_parts_str = '\n'.join(str(orderPart) for orderPart in self.orderParts)
        formatted_time = self.time.strftime("%Y-%m-%d %H:%M")  # Форматування часу до потрібного вигляду
        return f"Час замовлення: {formatted_time}\nКлієнт замовив:\n{order_parts_str}"

    def addOrderPart(self, orderPart):
        self.orderParts.append(orderPart)

    def getPrice(self):
        return sum(orderPart.getPrice() for orderPart in self.orderParts)

    def to_csv(self):
        with open("order.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Час замовлення", "Частина замовлення", "Ціна (гривні)"])
            for orderPart in self.orderParts:
                writer.writerow([self.time, orderPart.name, orderPart.getPrice()])

# Створюємо страви
risotto = Dish(name="Risotto alla milanese", price=250)
pizza = Dish(name="Margherita Pizza", price=300)
cola = Dish(name="Coca-Cola", price=50)

# Створюємо частини замовлення для страв
orderPart1 = OrderPart(id=1, name="Блюдо: ", dish=risotto)
orderPart2 = OrderPart(id=2, name="Блюдо: ", dish=pizza)
orderPart3 = OrderPart(id=3, name="Напій: ", dish=cola)

# Створюємо замовлення та вказуємо час замовлення
order = Order(time=datetime.now())

# Додаємо частини замовлення до замовлення
order.addOrderPart(orderPart1)
order.addOrderPart(orderPart2)
order.addOrderPart(orderPart3)

# Виводимо замовлення та ціну
print(order)
print(f"Загальна ціна замовлення: {order.getPrice()} гривень")

# Зберігаємо замовлення у CSV файл
order.to_csv()
