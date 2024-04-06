# Задача 1. Координаты точки
# В одной из практик предыдущего модуля была задача на реализацию класса «Точка».
# Модернизируйте класс по следующему условию: объект «Точка» на плоскости имеет
# координаты x и y; при создании новой точки могут передаваться пользовательские
# значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
# 1.	Предоставление информации о точке (используйте магический метод str).
# 2.	Геттер и сеттер для x.
# 3.	Геттер и сеттер для y.
# Для сеттеров реализуйте проверку на корректность входных данных: координаты должны
# быть числом.

class Dot:
    def __init__(self, x=None, y=None):
        self.__x = x if x else 0
        self.__y = y if y else 0

    def __str__(self):
        return f'({self.__x}; {self.__y})'

    def set_x(self, new_x):
        if isinstance(new_x, (int, float)):
            self.__x = new_x
            return self.__x
        else:
            raise Exception('Wrong input. "X" will be a digit.')

    def set_y(self, new_y):
        if isinstance(new_y, (int, float)):
            self.__y = new_y
            return self.__y
        else:
            raise Exception('Wrong input. "X" will be a digit.')

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


new_dot = Dot()
print('get_x(): ', new_dot.get_x())
print('get_y(): ', new_dot.get_y())
new_dot.set_x(123)
new_dot.set_y(456)
print('get_x(): ', new_dot.get_x())
print('get_y(): ', new_dot.get_y())
print('__str__(): ', new_dot.__str__())