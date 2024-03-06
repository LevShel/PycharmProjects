# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет,
# а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:
# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
# Напишите программу, которая выводит на экран следующие данные в разных строках:
# 1.	Все члены команды А, которые отдыхают.
# 2.	Все члены команды B, которые тренируются.
# 3.	Все члены команды C, которые путешествуют.

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

print('\n1. Все члены команды А, которые отдыхают:')
for key, value in players_dict.items():
    if value['team'] == 'A' and value['status'] == 'Rest':
        print(value['name'])
print('\n2. Все члены команды B, которые тренируются:')
for key, value in players_dict.items():
    if value['team'] == 'B' and value['status'] == 'Training':
        print(value['name'])
print('\n3. Все члены команды C, которые путешествуют:')
for key, value in players_dict.items():
    if value['team'] == 'C' and value['status'] == 'Travel':
        print(value['name'])