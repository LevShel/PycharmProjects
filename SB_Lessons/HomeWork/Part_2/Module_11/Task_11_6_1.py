# Задача 1. Драка
# Что нужно сделать
# Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.
# Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того,
# кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить
# сообщение, какой юнит атаковал и сколько у противника осталось здоровья. Как только
# у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том,
# кто одержал победу.
# Реализуйте такую программу.

import shutil
import random
import time


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 20
        self.death = False

    def is_attack(self):
        status = random.choice([True, False])
        if status:
            print(f'{self.name} is attack!\n')
            return self.attack
        else:
            print(f'{self.name} overslept attack...\n')
            return 0

    def get_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.death = True
            print(f'Warrior {self.name} is lose.\n')
        return self.health

    def print_info(self):
        print(f'{self.name}\t'
              f'Health: {self.health}\n')


def battle(w1, w2):
    queue = random.choice([w1, w2])
    if queue == w1:
        w2.get_damage(w1.is_attack())
        w2.print_info()
    elif queue == w2:
        w1.get_damage(w2.is_attack())
        w1.print_info()
    else:
        print('Something goes wrong...\n')


def new_round(w1, w2, i):
    print(f'\t\t\tRound {i}\n'
          f'{w1.name} [{w1.health}] - [{w2.health}] {w2.name}\n')
    return i


def end_round(i):
    i += 1
    print('=' * shutil.get_terminal_size().columns)
    time.sleep(3)
    return i


war_1 = Warrior('~ Warrior 1 ~')
war_2 = Warrior('~ Warrior 2 ~')

battle_round = 1
while not war_1.death and not war_2.death:
    battle_round = new_round(war_1, war_2, battle_round)
    battle(war_1, war_2)
    battle_round = end_round(battle_round)
