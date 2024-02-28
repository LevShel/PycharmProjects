# Задание 7. Считалка
# Что нужно сделать
# N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть
# в считалку на выбывание. Каждый K-й по счёту человек выходит из круга, после чего
# счёт продолжается со следующего за ним человека.
# На вход подаётся количество человек N и номер K. Напишите программу, которая выводит
# число от 1 до N — это номер человека, который останется в кругу последним.
# Пример:
# Количество человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7-й человек
#
# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2
#
# Текущий круг людей: [1, 3, 4, 5]
# Начало счёта с номера 3
# Выбывает человек под номером 5
#
# Текущий круг людей: [1, 3, 4]
# Начало счёта с номера 1
# Выбывает человек под номером 1
#
# Текущий круг людей: [3, 4]
# Начало счёта с номера 3
# Выбывает человек под номером 3
#
# Остался человек под номером 4

peoples = int(input('Num of peoples: '))
round_peoples = list(range(1, peoples+1))

shoot_num = int(input('Num in counter: '))
print(f'This means that every {shoot_num} person is eliminated.\n')

print('Current round of peoples:\n'
      f'{round_peoples}')
start_count = int(input('Start counting from: '))

# shoot_num %= len(round_peoples)

current_index = start_count - 1
while len(round_peoples) > 1:
    current_index = (current_index + shoot_num - 1) % len(round_peoples)
    eliminated_person = round_peoples.pop(current_index)
    print(f'\nEliminated person: {eliminated_person}')
    print('Current round of peoples:', round_peoples)

# def find_last_person(N, K):
#     people = list(range(1, N + 1))
#     index = 0
#     while len(people) > 1:
#         index = (index + K - 1) % len(people)
#         print(f'Выбывает человек под номером {people.pop(index)}')
#     return people[0]
#
# N = int(input('Количество человек: '))
# K = int(input('Какое число в считалке? '))
# print(f'Остался человек под номером {find_last_person(N, K)}')
