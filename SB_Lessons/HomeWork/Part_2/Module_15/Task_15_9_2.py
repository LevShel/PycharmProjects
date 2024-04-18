# Задача 2. Математический модуль
# Что нужно сделать
# Вася использует в своей программе очень много различных математических вычислений,
# связанных с фигурами. Например, нахождение их площадей или периметров. Поэтому, чтобы
# не захламлять код огромным количеством функций, он решил выделить для них отдельный класс,
# подключить как модуль и использовать по аналогии с модулем math.
# Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить
# и другие методы):
# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.
# Пример основного кода:
# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# print(res_1)
# print(res_2)
# Результат:
# 31.41592653589793
# 113.09733552923255

import math
from abc import ABC, abstractmethod


class MyMath(ABC):
    """
    Класс для различных математических вычислений,
    связанных с фигурами.
    Используется по аналогии с модулем math.
    """

    @abstractmethod
    def circle_len(radius: float) -> float:
        """
        Вычисляет длину окружности.
        Args:
            radius (float): r - радиус окружности.
        Returns:
            с (float): длина окружности.
        Formula:
            Длина окружности (C) вычисляется по формуле:
                C=2πr.
        Notes:
            math.pi (const): π - математическая постоянная (пи).
        """
        c = 2 * math.pi * radius
        return c

    @abstractmethod
    def circle_sq(radius: float) -> float:
        """
        Вычисляет площадь окружности.
        Args:
            radius (float): r - радиус окружности.
        Returns:
            a (float): площадь окружности.
        Formula:
            Площадь окружности (A) вычисляется по формуле:
                A = πr^2.
        Notes:
            math.pi (const): π - математическая постоянная (пи).
        """
        a = math.pi * (radius ** 2)
        return a

    @abstractmethod
    def qube_vol(side: float) -> float:
        """
        Вычисляет объём куба.
        Args:
            side (float): a - длина стороны куба.
        Returns:
            v (float): объём куба.
        Formula:
            Объём куба (V) вычисляется по формуле:
                V=a^3.
        """
        v = side ** 3
        return v

    @abstractmethod
    def sphere_sq(radius: float) -> float:
        """
        Вычисляет площадь поверхности сферы.
        Args:
            radius (float): r - радиус сферы.
        Returns:
            s (float): площадь поверхности сферы.
        Formula:
            Площадь поверхности сферы (S) вычисляется по формуле:
                S=4πr^2
        Notes:
            math.pi (const): π - математическая постоянная (пи).
        """
        s = 4 * math.pi * (radius ** 2)
        return s


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)  # 31.41592653589793
print(res_2)  # 113.09733552923255
