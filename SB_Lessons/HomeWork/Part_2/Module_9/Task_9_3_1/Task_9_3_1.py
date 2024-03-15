# Задача 1. Результаты
# Одному программисту дали задачу для обработки неких результатов тестирования
# двух групп людей. Файл первой группы (group_1.txt) находится в папке task,
# файл второй группы (group_2.txt) — в папке Additional_info.

# На экран нужно было вывести сумму очков первой группы, затем разность очков
# опять же первой группы и напоследок — произведение очков уже второй группы.
# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять.
# И оказалось, этот код просто не работает. Вот что он написал:
#
# file = open('E:\task\group_1.txt', 'read')
# summa = 0
# for i_line in file:
#     info = i_line.split()
#     summa += info[2]
# file = open('E:\task\group_1.txt', 'read')
# diff = 0
# for i_line in file:
#     info = i_line.split()
#     diff -= info[2]
# file_2 = open('E:\task\group_2.txt', 'read')
# compose = 0
# for i_line in file:
#     info = i_line.split()
#     compose *= info[2]
# print(summa)
# print(diff)
# print(compose)
#
# Исправьте код для решения поставленной задачи. Для проверки результата создайте
# необходимые папки (task, Additional_info, Dont touch me) на своём диске в соответствии
# с картинкой и также добавьте файлы group_1.txt и group_2.txt.

import os

file = open(os.path.join('task', 'group_1.txt'), 'r', encoding='utf-8')
summ = 0
diff = 0
for i_line in file:
    info = i_line.split()
    summ += int(info[2])
    diff -= int(info[2])
print(f'\t Group 1: \n'
      f'Sum of points: {summ}\n'
      f'Difference of points: {diff}')
file.close()

file = open(os.path.join('task', 'Additional_info', 'group_2.txt'), 'r', encoding='utf-8')
compp = 1
for i_line in file:
    info = i_line.split()
    compp *= int(info[2])
print(f'\t Group 2: \n'
      f'Compose of points: {compp}')
file.close()
