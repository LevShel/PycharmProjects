# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
# Также есть два дочерних класса:
# •	Солдат: получает урон, равный переданному значению.
# •	Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
# (а также инкапсуляции и наследования, конечно же).

class Unit:
    def __init__(self, damage=None):
        self.hp = 100
        self.damage = damage if damage else 0

    def get_damage(self, damage):
        pass


class Solder(Unit):
    def __init__(self):
        super().__init__()

    def get_damage(self, damage):
        self.damage = damage
        self.hp -= self.damage
        return self.hp

    def __str__(self):
        # super().get_damage(self.damage)
        print('Solder\n'
              f'damage = {self.damage}\n'
              f'hp = {self.hp}')


class Citizen(Unit):
    def __init__(self):
        super().__init__()

    def get_damage(self, damage):
        self.damage = damage * 2
        self.hp -= self.damage
        return self.hp

    def __str__(self):
        print('Citizen\n'
              f'damage = {self.damage}\n'
              f'hp = {self.hp}')


solder = Solder()
citizen = Citizen()
solder.__str__()
print()
solder.get_damage(11)
solder.__str__()
print()
citizen.__str__()
print()
citizen.get_damage(11)
citizen.__str__()
