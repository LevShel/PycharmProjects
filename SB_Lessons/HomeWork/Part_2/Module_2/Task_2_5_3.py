# Задание 3. Видеокарты
# Что нужно сделать
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений.
# Вместо полных названий хранятся только числа, которые обозначают модель и поколение
# видеокарты. Недавно компания выпустила новую линейку видеокарт. Самые старшие поколения
# разобрали за пару дней.
# Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.
# Пример:
# Количество видеокарт: 5
# Видеокарта 1: 3070
# Видеокарта 2: 2060
# Видеокарта 3: 3090
# Видеокарта 4: 3070
# Видеокарта 5: 3090
#
# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
# Новый список видеокарт: [ 3070 2060 3070 ]

cards = []
max_gen = 0
new_list = []
n = int(input('Количество видеокарт: '))
for i in range(1, n+1):
    card = int(input(f'Видеокарта {i}: '))
    cards.append(card)
    if card > max_gen:
        max_gen = card
print(f'Старый список видеокарт: {cards}')
for j in cards:
    if j != max_gen:
        new_list.append(j)
print(f'Новый список видеокарт: {new_list}')