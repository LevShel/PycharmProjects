# Задача 5. Песни
# Что нужно сделать
# Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти
# песен группы Depeche Mode. В информацию о каждом треке входит название
# и продолжительность с точностью до долей минут:
# violator_songs = [
# ['World in My Eyes', 4.86],
# ['Sweetest Perfection', 4.43],
# ['Personal Jesus', 4.56],
# ['Halo', 4.9],
# ['Waiting for the Night', 6.07],
# ['Enjoy the Silence', 4.20],
# ['Policy of Truth', 4.76],
# ['Blue Dress', 4.29],
# ['Clean', 5.83]
# ]
# Из этого списка Ваня хочет выбрать N песен и добавить их в особый плейлист
# с другими треками. При этом ему важно, сколько времени в сумме эти N песен будут звучать.
# Напишите программу, которая запрашивает у пользователя количество песен из списка
# и их названия, а на экран выводит общее время их звучания.
# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean
# Общее время звучания песен — 14,93 минуты

def select_song(num, song_list):
    name = input(f'Name of {i+1} song: ')
    for song in song_list:
        if name in song:
            # print(song)
            duration = float(song[1])
    return duration


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs = int(input('How much songs select? '))
total_duration = 0
for i in range(songs):
    total_duration += select_song(i, violator_songs)
print(f'Total duration: {round(total_duration, 2)} minutes.')
