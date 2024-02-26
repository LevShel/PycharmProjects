# Задача 1. Вода
# Одна бутылка воды «КлирВотер» от производителя «ВодЗавод» в разных магазинах
# стоит по-разному.
# Напишите программу, которая три раза вызывает функцию aboutWater, передаёт
# в неё один аргумент — цену на воду и выводит на экран название воды, производителя и цену.
#
# Пример:
# Название: КлирВотер
# Производитель: ВодЗавод
# Цена: 25
#
# Название: КлирВотер
# Производитель: ВодЗавод
# Цена: 30
#
# Название: КлирВотер
# Производитель: ВодЗавод
# Цена: 40

import random

def about_whater(price):
    print('Название: КлирВотер')
    print('Производитель: ВодЗавод')
    print(f'Цена: {price}\n')

for market in range(3):
    price = random.randint(25, 40)
    about_whater(price)

# price = 25
# about_whater(price)
# price = 30
# about_whater(price)
# price = 40
# about_whater(price)