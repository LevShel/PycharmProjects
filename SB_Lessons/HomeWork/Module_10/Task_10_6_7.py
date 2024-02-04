# Задание 7. Пирамидка-2
# Что нужно сделать
# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, за-полняя нечётными
# числами:
#            1
#          3    5
#       7    9     11
#    13   15    17    19
# 21   23    25    27    29

levels = int(input('Введите количество уровней пирамиды: '))

current_number = 1

for i in range(1, levels + 1):
    spaces = ' ' * (levels - i)
    row = ''

    for j in range(i):
        row += str(current_number) + ' '
        current_number += 2

    print(spaces + row.rstrip())
