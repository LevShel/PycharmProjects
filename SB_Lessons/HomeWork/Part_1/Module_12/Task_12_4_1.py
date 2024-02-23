# Задача 1. Среднее арифметическое
# Программа получает от пользователя два числа — a и b.
# Реализуйте функцию, которая принимает на вход числа a и b, считает
# и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b].
# Обеспечьте контроль ввода: не забывайте, что а всегда должно быть меньше, чем b.
# Пример:
# Введите левую границу: 3
# Введите правую границу: 8
# Среднее: 5.5
#
# Усложнение: сделайте это без использования циклов.

import math


def averrageNums(a, b):
    summ = 0
    nums = 0

    nums = math.floor(b) - math.ceil(a) + 1
    next_num = math.ceil(a)
    for i in range(nums):
        summ += next_num
        next_num += 1
    average = summ / nums

    print(f'Среднее: {average}')


while True:
    a = float(input('Введите левую границу: '))
    b = float(input('Введите правую границу: '))
    if a < b:
        averrageNums(a, b)
        break
    else:
        print('\nError. Enter a < b.\n')