# Задача 5. Совместное проживание
# Что нужно сделать
# Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве,
# Артём решил провести необычное исследование. Для этого он реализовал модель человека
# и модель дома.
# Человек может (должны быть такие методы):
# •	есть (+ сытость, − еда);
# •	работать (− сытость, + деньги);
# •	играть (− сытость);
# •	ходить в магазин за едой (+ еда, − деньги);
# •	прожить один день (выбирает одно действие согласно описанному ниже приоритету
# и выполняет его).
# У человека есть (должны быть такие атрибуты):
# •	имя,
# •	степень сытости (изначально 50),
# •	дом.
# В доме есть:
# •	холодильник с едой (изначально 50 еды),
# •	тумбочка с деньгами (изначально 0 денег).
# Если сытость человека становится меньше нуля, человек умирает.
# Логика действий человека определяется следующим образом:
# 1.	Генерируется число кубика от 1 до 6.
# 2.	Если сытость < 20, то нужно поесть.
# 3.	Иначе, если еды в доме < 10, то сходить в магазин.
# 4.	Иначе, если денег в доме < 50, то работать.
# 5.	Иначе, если кубик равен 1, то работать.
# 6.	Иначе, если кубик равен 2, то поесть.
# 7.	Иначе играть.
# По такой логике эксперимента человеку надо прожить 365 дней.
# Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте
# работу программы несколько раз.
# Советы и рекомендации
# •	В большинстве случаев классы нужны не для того, чтобы с ними работать напрямую,
# а чтобы с их помощью создавать объекты, которые будут содержать необходимую информацию
# и смогут вызывать нужные методы. Наш случай не исключение: вам не нужно работать
# напрямую с классами, работайте с объектами, которые создаются при помощи этих классов.
# •	Глобальные переменные создают зависимости. Чем больше класс обращается к переменным,
# созданным снаружи класса, тем больше в классе появляется неопределённости (для работы
# с классом вам придётся отслеживать значения всех этих переменных).
# По возможности передавайте нужные данные в объект и записывайте их в атрибуты вместо
# обращения к глобальной переменной.

import random
import shutil
import time


class Human:
    def __init__(self, name):
        self.live = True
        self.name = name  # имя
        self.satiety = 50  # степень сытости (изначально 50)
        if self.satiety == 0:  # Если сытость человека становится меньше нуля, человек умирает
            self.live = False
        self.house = House()  # дом

    def eating(self):  # есть (+ сытость, − еда)
        if self.house.fridge >= 1:
            self.satiety += 1
            self.house.fridge -= 1
            print(f'{self.name} ate and now his satiety level is: {self.satiety}.\n'
                  f'There are {self.house.fridge} of food in fridge.')
        elif self.satiety >= 1 > self.house.fridge:
            print(f'There are {self.house.fridge} of food in fridge.\n'
                  f'{self.name} ate and now his satiety level is: {self.satiety}.')
        else:
            print(f'There are {self.house.fridge} of food in fridge.\n'
                  f'{self.name} died of starvation.')
            self.live = False
            return self.died()

    def working(self):  # работать (− сытость, + деньги)
        self.satiety -= 1
        self.house.money += 1
        print(f'{self.name} worked and now his satiety level is: {self.satiety}.\n'
              f'There are {self.house.money} of money in bedside table.')

    def playing(self):  # играть (− сытость)
        self.satiety -= 1
        print(f'{self.name} played and now his satiety level is: {self.satiety}.')

    def shopping(self):  # ходить в магазин за едой (+ еда, − деньги)
        if self.house.money >= 1:
            self.house.fridge += 1
            self.house.money -= 1
            print(f'{self.name} shopped and now there are {self.house.fridge} of food in fridge.\n'
                  f'And there are {self.house.money} of money in bedside table.')
        else:
            print('There aren`t any money to buy some food...')

    def life_a_day(
            self):  # прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его)
        action = random.randint(1, 6)
        if action == 1:  # если кубик равен 1, то работать
            return self.working()
        elif action == 2:  # если кубик равен 2, то поесть
            return self.eating()
        elif action not in [1, 2]:
            if self.satiety <= 20:  # Если сытость < 20, то нужно поесть
                return self.eating()
            elif self.house.fridge < 10:  # Иначе, если еды в доме < 10, то сходить в магазин
                return self.shopping()
            elif self.house.money < 50:  # Иначе, если денег в доме < 50, то работать
                return self.working()
            else:  # Иначе играть
                return self.playing()

    def died(self):
        self.live = False
        print('Game over!\n'
              'You died...')

    def print_info(self):
        print(f'\tName: {self.name}\n'
              f'\tSatiety: {self.satiety}\n'
              f'\tMoney in bedside table: {self.house.money}\n'
              f'\tFood in fridge: {self.house.fridge}')


class House:
    def __init__(self):
        self.fridge = 50  # холодильник с едой (изначально 50 еды)
        self.money = 0  # тумбочка с деньгами (изначально 0 денег)


def save_to_file(human, i):
    if i == 1:
        with open(f'satiety.txt', 'w') as file:
            file.write(f'{str(i)}\t{str(human.satiety)}\n')
        with open(f'money.txt', 'w') as file:
            file.write(f'{str(i)}\t{str(human.house.money)}\n')
        with open(f'food.txt', 'w') as file:
            file.write(f'{str(i)}\t{str(human.house.fridge)}\n')
    else:
        with open(f'satiety.txt', 'a') as file:
            file.write(f'{str(i)}\t{str(human.satiety)}\n')
        with open(f'money.txt', 'a') as file:
            file.write(f'{str(i)}\t{str(human.house.money)}\n')
        with open(f'food.txt', 'a') as file:
            file.write(f'{str(i)}\t{str(human.house.fridge)}\n')


def new_day(human, i):
    print(f'\t\t\tDay {i}')
    human.life_a_day()
    human.print_info()
    save_to_file(human, i)
    return i


def end_day(i):
    i += 1
    print('=' * shutil.get_terminal_size().columns)
    time.sleep(1)
    return i


boy = Human('Lev')
girl = Human('Girlfriend')
flat = House()
boy.house = flat
girl.house = flat

day = 1
while (boy.live and girl.live) or day == 366:
    day = new_day(boy, day)
    day = new_day(girl, day)
    day = end_day(day)
