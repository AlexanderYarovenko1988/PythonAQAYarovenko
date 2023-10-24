import datetime

"""
Задача 1
Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів. 
Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int), і знак(True або False, які репрезентують + і -). 
Повертає datetime. 
В цій задачі скористайтесь datetime.timedelta
"""

def add_or_subtract_days(date, days, sign):
  """
  Додає або віднімає від заданої дати певну кількість днів.

  Приймає на вхід:
    date: будь-яку дату та час (datetime)
    days: значення днів (int)
    sign: знак (True або False, які репрезентують + і -)

  Повертає:
    datetime
  """

  delta = datetime.timedelta(days=days)
  if sign:
    return date + delta
  else:
    return date - delta


# Приклад використання

date = datetime.datetime(2023, 10, 24, 16, 45, 24)

print("-------------- Задача 1 ------------------")
# Додаємо 5 днів
new_date = add_or_subtract_days(date, 5, True)
print(new_date)

# Віднімаємо 10 днів
new_date = add_or_subtract_days(date, 10, False)
print(new_date)
print("-------------- Задача 2 ------------------")

"""
Задача 2
Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), 
вираховуючі різницю між наданим значеням і значенням datetime.now(). 
Приймає дату та час(datetime), повертає два значення: datetime і datetime.timestamp. 
В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль
"""

import datetime

def calculate_age(birthdate):
  """
  Вираховує точний вік.

  Приймає на вхід:
    birthdate: дата народження (datetime)

  Повертає:
    datetime: поточна дата
    datetime.timestamp: поточний час у секундах
  """

  current_date = datetime.datetime.now()
  difference = current_date - birthdate
  age_in_seconds = difference.total_seconds()

  return current_date, age_in_seconds

# Приклад використання

birthdate = datetime.datetime(1988, 1, 7, 0, 0, 0)
current_date, age_in_seconds = calculate_age(birthdate)

# Присвоюємо вік у роках новій змінній
age_in_years = int(age_in_seconds / (365.2425 * 24 * 60 * 60))

print(f"Ваш вік: {age_in_years} роки")

print("-------------- Задача 3 ------------------")
"""
Створіть за допомогою list comprehension список, в якому буде 100 елементів,
і кожен із яких буде в границях від 1 до 10(для цього можна скористатись функцією randint із модуля random). 
Порахуйте кількість кожного елемента і виведіть в консоль
"""

import random

# Створюємо список з 100 елементів
numbers = [random.randint(1, 10) for _ in range(100)]

# Порахуємо кількість кожного елемента
counts = {}
for number in numbers:
  if number in counts:
    counts[number] += 1
  else:
    counts[number] = 1

# Виводимо кількість кожного елемента в консоль
for number, count in counts.items():
  print(f"Число {number} зустрічається {count} разів")





