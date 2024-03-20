# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
# •	цвет машины (например, красный),
# •	цена (один миллион),
# •	максимальная скорость (200),
# •	текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости
# на случайное число от нуля до 200.

import random


class Car:
    def __init__(self):
        self.color = 'red'
        self.price = 1000000
        self.max_speed = 200
        self.current_speed = 0

    def set_current_speed(self):
        self.current_speed = random.randint(0, 200)

    def print_info(self):
        print(f'Color: {self.color}\n'
              f'Price: {self.price}\n'
              f'Max speed: {self.max_speed}\n'
              f'Current speed: {self.current_speed}\n')


car_1 = Car()
car_1.set_current_speed()
car_1.print_info()

car_2 = Car()
car_2.set_current_speed()
car_2.print_info()

car_3 = Car()
car_3.set_current_speed()
car_3.print_info()
