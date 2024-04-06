# Задача 1. Корабли
# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя
# модель, и каждый может сделать два действия: сообщить свою модель и идти по воде.
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# У него есть ещё два действия: погрузить и выгрузить груз с корабля.
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся
# вместе с моделью. Также, вместо погрузки и выгрузки, у него есть другое действие —
# атаковать.
# Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты
# и методы в отдельный класс «Корабль» и используйте наследование. Не забудьте
# про функцию super в дочерних классах.

class Ship:
    """
    Базовый класс, описывающий корабль.
    Args:
        model (str): передаётся название модели.
    Attributes:
        move (str): состояние движения корабля. По-умолчанию корабль стоИт.
    """
    def __init__(self, model):
        """
        Функция инициализации.
        """
        self.__model = model
        self.move = 'Ship is standing.'

    def __str__(self):
        """
        Функция для вывода названия модели.
        """
        return f'Model of ship: {self.__model}.'

    def sail(self):
        """
        Функция для установки движения.
        """
        if self.__model == 'Russian warship':
            self.move = 'Russian warship goes na hui =)'
        else:
            self.move = 'Ship is going now.'
        return self.move


class WarShip(Ship):
    """
    Класс военного корабля. Родитель: Ship.
    Args:
        model (str): передаётся название модели.
    Attributes:
        gun (str): тип оружия на борту.
    """
    def __init__(self, model, gun):
        """
        Функция инициализации.
        """
        super().__init__(model)
        self.gun = gun

    def attack(self):
        """
        Функция для вывода названия оружия, которым атакует корабль.
        """
        return f'Ship attacks by {self.gun}'


class CargoShip(Ship):
    """
    Класс грузового корабля. Родитель: Ship.
    Args:
        model (str): передаётся название модели.
    Attributes:
        fullness (int): заполненность корабля. По-умолчанию корабль пустой.
    """
    def __init__(self, model):
        """
        Функция инициализации.
        """
        super().__init__(model)
        self.fullness = 0

    def loading(self):
        """
        Функция погрузки (загрузки) груза на корабль.
        Атрибут fullness (int) увеличивается на 1.
        """
        self.fullness += 1
        return self.fullness

    def unloading(self):
        """
        Функция разгрузки корабля.
        Атрибут fullness (int) устанавливается равным 0.
        Если корабль уже пустой, то выводится соответствующее сообщение.
        """
        if self.fullness > 0:
            self.fullness = 0
            return self.fullness
        else:
            print('Ship is already empty.')


# Создание кораблей:
ship_1 = WarShip(gun='cannons', model='K3LJ5B')
ship_2 = CargoShip(model='LIG34TH')
ship_3 = WarShip(model='Russian warship', gun='torpedoes')
# Вывод информации о соданных кораблях:
print(ship_1.__str__())
print(ship_2.__str__())
print(ship_3.__str__())
# Попытка разгрузить и загрузить корабль. Вывод информации о загруженности:
ship_2.unloading()
print('Fullness of ship: ', ship_2.fullness)
ship_2.loading()
print('Fullness of ship: ', ship_2.fullness)
# Начало движения кораблей:
print(ship_1.sail())
print(ship_3.sail())
print(ship_2.sail())
