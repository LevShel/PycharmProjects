# Задача 6. Абстрактный класс
# Контекст
# Вы работаете в компании, занимающейся разработкой программного обеспечения для архитектурных проектов. Вам необходимо
# разработать программу для расчёта площади различных геометрических фигур, таких как круги, прямоугольники
# и треугольники.
# Задача
# Создайте:
# класс Shape, который будет базовым классом для всех фигур и будет хранить пустой метод area, который наследники
# должны переопределить;
# класс Circle;
# класс Rectangle;
# класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод для вычисления площади фигуры.
# Дополнительно: изучите информацию о работе с абстрактными классами.
# На основе этой информации сделайте так, чтобы:
# Нельзя было создавать объекты класса Shape.
# Наследники класса Shape переопределяли его метод area, чтобы объекты этих классов можно было использовать.

import math


class __Shape:
    def __init__(self, a=None, b=None, c=None, p=None, r=None):
        self.a = a if a else None
        self.b = b if b else None
        self.c = c if c else None
        self.p = p if p else None
        self.r = r if r else None

    def circle_area(self):
        return round(math.pi * (self.r ** 2), 2)

    def rectangle_area(self):
        return round(self.a * self.b, 2)

    def triangle_area(self):
        return round(math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)), 2)

    def area(self):
        if isinstance(self, Circle):
            return self.circle_area()
        elif isinstance(self, Rectangle):
            return self.rectangle_area()
        elif isinstance(self, Triangle):
            return self.triangle_area()


class Circle(__Shape):
    def __init__(self, r):
        super().__init__(r=r)


class Rectangle(__Shape):
    def __init__(self, a, b):
        super().__init__(a=a, b=b)


class Triangle(__Shape):
    def __init__(self, a, b, c):
        p = (a + b + c) / 2
        super().__init__(a=a, b=b, c=c, p=p)


choice = int(input('Choose figure:\n'
                   '\t1. Circle\n'
                   '\t2. Rectangle\n'
                   '\t3. Triangle\n'
                   '>: '))
if choice == 1:
    r = float(input('\n r = '))
    fig = Circle(r)
    print(f'\nCircle area is: {fig.area()}')
elif choice == 2:
    a = float(input('\n a = '))
    b = float(input(' b = '))
    fig = Rectangle(a, b)
    print(f'\nRectangle area is: {fig.area()}')
elif choice == 3:
    a = float(input('\n a = '))
    b = float(input(' b = '))
    c = float(input(' c = '))
    fig = Triangle(a, b, c)
    print(f'\nTriangle area is: {fig.area()}')
else:
    exit()
