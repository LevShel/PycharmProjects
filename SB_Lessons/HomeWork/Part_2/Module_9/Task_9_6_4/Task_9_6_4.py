# Задача 4. Турнир
# Что нужно сделать
# В файле first_tour.txt записано число K и данные об участниках турнира
# по настольной игре «Орлеан»: фамилии, имена и количество баллов,
# набранных в первом туре. Во второй тур проходят участники,
# которые набрали более K баллов в первом туре.
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников,
# прошедших во второй тур, с нумерацией.
# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура.
# Затем программа должна вывести фамилии, инициалы и количество баллов всех участников,
# прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы.
# Список должен быть отсортирован по убыванию набранных баллов.
# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

file = open('first_tour.txt', 'r')
data = [i_str for i_str in file]
file.close()

k = int(data[0])
# 80

list_players = []
for player in range(1, len(data)):
    list_players.append(data[player].split(' '))
# [['Ivanov', 'Serg', '80\n'], ['Sergeev', 'Petr', '92\n'], ['Petrov', 'Vasiliy', '98\n'], ['Vasiliev', 'Maxim', '78']]

list_second_tour = []
for player_info in list_players:
    if int(player_info[2]) > k:
        name = player_info[1][0]+'. '
        surname = player_info[0]+' '
        scores = player_info[2]
        player = name+surname+scores
        list_second_tour.append(player)
# ['P. Sergeev 92\n', 'V. Petrov 98\n']

num_players = len(list_second_tour)
# 2

list_second_tour.sort(key=lambda x: int(x.split()[-1]), reverse=True)
# ['V. Petrov 98\n', 'P. Sergeev 92\n']

file = open('second_tour.txt', 'w')
file.write(str(num_players)+'\n')
place = 1
for player in list_second_tour:
    file.write(str(place) + ') ' + str(player))
    place += 1
file.close()
