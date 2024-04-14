# Задача 1. Транспорт
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы. Класс «Транспорт» должен быть абстрактным
# и содержать абстрактные методы.
# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»

from abc import ABC, abstractmethod


class MusicMixin:
    def play_music(self, song: str) -> None:
        print(f"Playing '{song}'")


class Transport(ABC):
    def __init__(self, color: str) -> None:
        self.color = color

    @abstractmethod
    def move(self) -> None:
        pass


class Cars(Transport):
    """ Автомобили. Они могут ездить только по земле """

    def __init__(self, color: str) -> None:
        super().__init__(color)

    def move(self) -> None:
        print(f"Moving on ground with speed {self.speed}")


class Ships(Transport):
    """ Лодки. Ездят только по воде """

    def __init__(self, color: str) -> None:
        super().__init__(color)

    def move(self) -> None:
        print(f"Moving on water with speed {self.speed}")


class Amphibian(Transport, MusicMixin):
    """ Амфибии. Могут перемещаться и по земле, и по воде """

    def __init__(self, color: str) -> None:
        super().__init__(color)

    def move(self) -> None:
        # super(MusicMixin).play_music('Make some Noize')
        print(f"Moving on ground with speed {self.ground_speed}")
        print(f"Moving on water with speed {self.water_speed}")


my_car = Cars("Red")
my_car.speed = 240
my_car.move()  # Moving on ground with speed 100

my_boat = Ships("Yellow")
my_boat.speed = 150
my_boat.move()  # Moving on water with speed 50

my_amphibian = Amphibian("Green")
my_amphibian.ground_speed = 111
my_amphibian.water_speed = 77
my_amphibian.move()  # Moving on ground with speed 80\nMoving on water with speed 40
my_amphibian.play_music('Make some Noize')
