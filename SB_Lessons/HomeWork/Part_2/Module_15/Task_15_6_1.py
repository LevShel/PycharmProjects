# Задача 1. Транспорт 2
# Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс геттерами и сеттерами
# для соответствующих атрибутов. Используйте встроенные декораторы. Вот входные данные той задачи:
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.

from abc import ABC, abstractmethod


class MusicMixin:
    def play_music(self, song: str) -> None:
        print(f"Playing '{song}'")


class Transport(ABC):
    def __init__(self, color: str) -> None:
        self.color = color

    @abstractmethod
    def speed(self) -> None:
        pass


class Cars(Transport):
    """ Автомобили. Они могут ездить только по земле """

    def __init__(self, color: str, speed: int) -> None:
        super().__init__(color)
        self._speed = speed

    @property
    def speed(self) -> str:
        return f'CAR Moving on ground with speed {self._speed}'

    @speed.setter
    def speed(self, new_speed) -> int:
        if new_speed >= 0:
            self._speed = new_speed
            return self._speed
        else:
            raise Exception('Wrong speed!')


class Ships(Transport):
    """ Лодки. Ездят только по воде """

    def __init__(self, color: str, speed: int) -> None:
        super().__init__(color)
        self._speed = speed

    @property
    def speed(self) -> str:
        return f'SHIP Moving on ground with speed {self._speed}'

    @speed.setter
    def speed(self, new_speed) -> int:
        if new_speed >= 0:
            self._speed = new_speed
            return self._speed
        else:
            raise Exception('Wrong speed!')


class Amphibian(Transport, MusicMixin, ABC):
    """ Амфибии. Могут перемещаться и по земле, и по воде """

    def __init__(self, color: str, speed: int) -> None:
        super().__init__(color, speed, speed)
        # self._water_speed = water_speed
        # self._ground_speed = ground_speed

    @property       # TODO
    def speed(self) -> str:
        return f'AMPHIBIAN Moving on ground with speed {self.speed}'

    @speed.setter       # TODO
    def speed(self, new_speed) -> int:
        if new_speed >= 0:
            self.speed = new_speed
            return self.speed
        else:
            raise Exception('Wrong speed!')

    # @property
    # def ground_speed(self) -> str:
    #     return f'Moving on ground with speed {self.speed}'
    #
    # @property
    # def water_speed(self) -> str:
    #     return f'Moving on water with speed {self._water_speed}'
    #
    # @ground_speed.setter
    # def ground_speed(self, new_speed) -> int:
    #     if new_speed >= 0:
    #         self.speed = new_speed
    #         return self._ground_speed
    #     else:
    #         raise Exception('Wrong speed!')
    #
    # @water_speed.setter
    # def water_speed(self, new_speed) -> int:
    #     if new_speed >= 0:
    #         self._water_speed = new_speed
    #         return self._water_speed
    #     else:
    #         raise Exception('Wrong speed!')


my_car = Cars(color="Red", speed=240)
my_car.speed = 300
print(my_car.speed)  # Moving on ground with speed 100

my_boat = Ships(color="Yellow", speed=150)
my_boat.speed = 200
print(my_boat.speed)  # Moving on water with speed 50

my_amphibian = Amphibian(color="Green", speed=111)
my_amphibian.ground_speed = 120
my_amphibian.water_speed = 80
print(my_amphibian.ground_speed,
      my_amphibian.water_speed)  # Moving on ground with speed 80\nMoving on water with speed 40
my_amphibian.play_music('Make some Noize')
