# Задача 3. May the force be with you
# Что нужно сделать
# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. Ссылка на документацию: Documentation.
# Внимательно изучите документацию этого API и напишите программу, которая выводит на экран (и в JSON-файл)
# информацию о пилотах легендарного корабля Millennium Falcon.
# Информация о корабле должна содержать следующие пункты:
# название,
# максимальная скорость,
# класс,
# список пилотов.
# Внутри списка о каждом пилоте должна быть следующая информация:
# имя,
# рост,
# вес,
# родная планета,
# ссылка на информацию о родной планете.

import json
import requests

# info = requests.get('https://swapi.dev/api/starships/10/')
# print(info.text)
#
# info_json = json.loads(info)
# with open('info.json', 'w') as file:
#     json.dump(info_json, file, indent=4)

with open('info.json', 'r') as file:
    data = json.load(file)

print('название:', data['name'])
print('максимальная скорость', data['max_atmosphering_speed'])
print('класс:', data['starship_class'])
# TODO:
print("список пилотов:")
print('имя,')
print('рост,')
print('вес,')
print('родная планета,')
print('ссылка на информацию о родной планете.')