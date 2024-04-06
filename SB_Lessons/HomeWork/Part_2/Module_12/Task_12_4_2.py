# Задача 2. Полёт
# Иногда для реализации дочерних классов используется так называемый класс-роль,
# где также описываются общие атрибуты и методы, но в программе инициализируются
# объекты только дочерних классов, а базовый класс-роль не трогается. К примеру,
# что общего у бабочки и ракеты? Они обе могут летать и приземляться.
#
# Реализуйте класс «Может летать».
# Атрибуты:
# •	Высота = 0.
# •	Скорость = 0.
# Методы:
# •	Взлететь (в теле прописать pass).
# •	Лететь (в теле прописать pass).
# •	Приземлиться (установить высоту и скорость в значение 0).
# •	Вывести высоту и скорость на экран.
#
# Затем реализуйте два дочерних класса:
# «Бабочка», который может:
# •	Взлететь (высота = 1).
# •	Лететь (скорость = 0.5).
# «Ракета», которая может:
# •	Взлететь (высота = 500, скорость = 1000).
# •	Приземлиться (высота = 0, взрыв).
# •	Взорваться (тут уже что угодно).

class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def fly_up(self):
        pass

    def flying(self):
        pass

    def landing(self):
        self.height = 0
        self.speed = 0

    def print_info(self):
        print(f'Current height: {self.height}\t current speed: {self.speed}')


class Butterfly(CanFly):
    def fly_up(self):
        self.height = 1

    def flying(self):
        self.speed = 0.5


class Rocket(CanFly):
    def fly_up(self):
        self.height = 500
        self.speed = 1000

    def landing(self):
        self.explosion()

    def explosion(self):
        self.height = 0
        self.speed = 0
        print('The rocket exploded.')


print('\nBUTTERFLY:')
btfl = Butterfly()
btfl.print_info()
print('\tfly up')
btfl.fly_up()
btfl.print_info()
print('\tflying')
btfl.flying()
btfl.print_info()
print('\tlanding')
btfl.landing()
btfl.print_info()
print('\nROCKET:')
rckt = Rocket()
rckt.print_info()
print('\tfly up')
rckt.fly_up()
rckt.print_info()
print('\tflying')
rckt.flying()
rckt.print_info()
print('\tlanding')
rckt.landing()
rckt.print_info()