#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # Случайное число от -10 до 10

# Допишите код для проверки значения переменной number
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
