# Задача 2. Роботы
# На военную базу завезли несколько интересных моделей роботов, которые похожи между
# собой, но имеют немного разные функции. У каждого робота есть номер модели и действие
# operate, которое означает, что делает робот. Особенности роботов следующие:
# •	У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде
# operate робот сообщает, что он пылесосит пол, и выводит текущую заполняемость мешка.
# •	У военного робота есть оружие, и при команде operate он выводит сообщение о защите
# военного объекта с помощью этого оружия.
# Ещё есть робот — подводная лодка, который также является военным. У этого робота
# есть значение глубины, и при команде operate он делает то же, что и военный робот,
# плюс сообщает, что охрана ведётся под водой.
# Напишите программу, которая реализует все необходимые классы роботов.

class Robot:
    def __init__(self, model):
        self.model = model

    def operate(self):
        pass

    def __str__(self):
        return f'{self.model}\t{self.operate}'


class RobotCleaner(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.trashbox = 0

    def operate(self):
        print(f'RC "{self.model}" is cleaning now.', end=' ')
        self.trashbox += 1
        print(f'Trashbox filled on {self.trashbox}.')
        return self.trashbox


class WarRobot(Robot):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self):
        print(f'WR "{self.model}" is defending by {self.weapon}.')


class SubmarineRobot(WarRobot):
    def __init__(self, model, weapon, deepness=None):
        super().__init__(model, weapon)
        self.deepness = deepness if deepness else -100500

    def operate(self):
        print(f'SMWR "{self.model}" is defending by {self.weapon} under water at {self.deepness}.')


r1 = RobotCleaner(model='Xiaomi VC 1S')
r2 = WarRobot(model='Terminator', weapon='gun')
r3 = SubmarineRobot(model='Yellow', weapon='torpedoes')

r1.operate()
r2.operate()
r3.operate()