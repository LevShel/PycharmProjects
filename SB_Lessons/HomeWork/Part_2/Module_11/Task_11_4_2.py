# Задача 2. Координаты точки
# Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут
# передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
# Реализуйте класс, который будет представлять эту точку, и напишите метод, который
# предоставляет информацию о ней. Также внутри класса пропишите счётчик, который будет
# отвечать за количество созданных точек.
# Подсказка: счётчик можно объявить внутри самого класса и увеличивать его
# в методе __init__.

class Dot():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.i = 1

    def create_new_dot(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.i += 1
        return self.x, self.y, self.i

    def print_info(self):
        print(f'x = {self.x}\n'
              f'y = {self.y}\n'
              f'dots: {self.i}\n')


dot = Dot()
dot.print_info()
dot.create_new_dot(5, 8)
dot.print_info()
dot.create_new_dot(4, 6)
dot.print_info()

