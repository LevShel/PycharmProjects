# Задача 1. Новые списки
# Что нужно сделать
# Даны три списка:
from typing import List
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
# Из списка names берутся только имена минимум из пяти букв.
# Из списка numbers берётся произведение всех чисел.

from functools import reduce

print('\n')

new_floats: List[float] = list(map(lambda num: round(num ** 3, 3), floats))
print(floats, '\n', new_floats)

print('\n')

new_names: List[str] = list(filter(lambda name: len(name) >= 5, names))
print(names, '\n', new_names)

print('\n')

new_numbers: int = reduce(lambda a, b: a * b, numbers, 1)
print(numbers, '\n', new_numbers)
