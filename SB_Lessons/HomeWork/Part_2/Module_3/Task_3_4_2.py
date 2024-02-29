# Задача 2. Олимпиада
# В олимпиаде по программированию участвует N человек, в списке участников
# они обозначаются под номерами 1, 2, 3, 4 и так далее до N. Эти участники поделены
# на команды по K человек.
# Напишите программу, которая принимает на вход количество участников и количество
# человек в каждой команде, затем генерирует список таких команд и выводит его на экран.
# Обеспечьте контроль ввода: в каждой команде должно быть ровно по K человек.
#
# Пример 1:
# Кол-во участников: 12
# Кол-во человек в команде: 4
#
# Общий список команд: [[1, 2 ,3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# Пример 2:
# Кол-во участников: 12
# Кол-во человек в команде: 5
#
# 12 участников невозможно поделить на команды по 5 человек!

total_teams = []
player = 1
participants = int(input('Num of participants: '))
team_players = int(input('Num of players in team: '))
if participants % team_players == 0:
    for i in range(1, int(participants/team_players)+1):
        team = []
        for j in range(player, player+team_players):
            team.append(j)
        player += team_players
        total_teams.append(team)
    print(f'Total list of teams: {total_teams}')
else:
    print(f'{participants} participants cannot be divided into '
          f'teams of {team_players} people!')

