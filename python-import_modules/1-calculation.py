#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # Случайное число от -10000 до 10000
last_digit = number % 10  # Последняя цифра числа

# Если число отрицательное, берем абсолютное значение последней цифры
if number < 0:
    last_digit = -last_digit

# Печатаем нужный результат в зависимости от последней цифры
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

