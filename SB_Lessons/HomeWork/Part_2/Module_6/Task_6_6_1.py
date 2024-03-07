# Задание 1. Песни — 2
# Что нужно сделать
# Продолжим писать приложение для удобного прослушивания музыки, но теперь песни
# хранятся в виде словаря, а не в виде вложенных списков. Каждая песня состоит
# из названия и продолжительности с точностью до долей минут.
# violator_songs = {
# 'World in My Eyes': 4.86,
# 'Sweetest Perfection': 4.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.9,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.20,
# 'Policy of Truth': 4.76,
# 'Blue Dress': 4.29,
# 'Clean': 5.83
# }
# Напишите программу, которая запрашивает у пользователя количество песен из списка
# и их названия, а на экран выводит общее время их звучания.
# Пример
# Сколько песен выбрать? 3
# Название первой песни: Halo
# Название второй песни: Enjoy the Silence
# Название третьей песни: Clean
# Общее время звучания песен: 14,93 минуты

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_songs = int(input('How many songs to choose: '))
list_songs = [input(f'Name of {i} song: ') for i in range(1, num_songs + 1)]
duration = sum(violator_songs[song] for song in list_songs if song in violator_songs)
print(f'Total duration is {round(duration, 2)} min.')
