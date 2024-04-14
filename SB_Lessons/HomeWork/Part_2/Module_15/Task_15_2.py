# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких, а летающих: разведывательного дрона
# и военного робота.
# Разведывательный дрон просто летает в поиске противника. При команде operate он выводит сообщение «Веду разведку
# с воздуха» и передвигается немного вперёд.
# У летающего военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта
# с воздуха с помощью этого оружия.
# Напишите программу, которая реализует все необходимые классы роботов. Сущности «Робот» и «Может летать» должны быть
# вынесены в отдельные классы. Обычный робот имеет модель и может вывести сообщение «Я — Робот». Объект, который умеет
# летать, дополнительно имеет атрибуты «Высота» и «Скорость», а также может взлетать, летать и приземляться.


class Robot:
    """
    Simple robot.
    Обычный робот имеет модель
    и может вывести сообщение «Я — Робот».
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def operate(self) -> None:
        pass

    def robot_info(self) -> str:
        return ('I`m Robot {name}.'.format(
            name=self.name
        ))


class CanFly:
    """Fact about flying"""

    def __init__(self, height: int = None, speed: int = None, distance: int = None) -> None:
        self.height = height if height else 0
        self.speed = speed if speed else 0
        self.distance = distance if distance else 0

    def set_height(self, new_height: int) -> int:
        self.height = new_height
        return self.height

    def set_speed(self, new_speed: int) -> int:
        self.speed = new_speed
        return self.speed

    def move_forward(self) -> int:
        self.distance += 1
        return self.distance

    def can_fly_info(self) -> str:
        return ('Current:\n\theight: {height}\n\tspeed: {speed}\n\tdistance: {distance}'.format(
            height=self.height,
            speed=self.speed,
            distance=self.distance
        ))


class SpyRobot(Robot, CanFly):
    """
    Разведывательный дрон просто летает в поиске противника.
    При команде operate он выводит сообщение «Веду разведку
    с воздуха» и передвигается немного вперёд.
    """

    def __init__(self, name: str, height: int = None, speed: int = None, distance: int = None) -> None:
        Robot.__init__(self, name)
        CanFly.__init__(self, height, speed, distance)

    def operate(self) -> None:
        self.move_forward()
        self.set_height(new_height=1000)
        self.set_speed(new_speed=123)
        print('{robot} Веду разведку с воздуха!\n'
              '{fly_info}'.format(
                robot=self.robot_info(),
                fly_info=self.can_fly_info()
              ))


class WarRobot(Robot, CanFly):
    """
    У летающего военного робота есть оружие,
    и при команде operate он выводит сообщение
    о защите военного объекта с воздуха с помощью этого оружия.
    """

    def __init__(self, name: str, height: int = None, speed: int = None, distance: int = None,
                 weapon: str = None) -> None:
        Robot.__init__(self, name)
        CanFly.__init__(self, height, speed, distance)
        self.weapon = weapon

    def operate(self) -> None:
        self.set_height(new_height=500)
        self.set_speed(new_speed=0)
        print(
            '{robot} Защищаю военный объект с воздуха с помощью {weapon}!\n'
            '{fly_info}'.format(
                robot=self.robot_info(),
                fly_info=self.can_fly_info(),
                weapon=self.weapon
            ))


my_spy_robot = SpyRobot(name='Spyer')
my_spy_robot.operate()

my_war_robot = WarRobot(name='Warrior', weapon='bomb')
my_war_robot.operate()
