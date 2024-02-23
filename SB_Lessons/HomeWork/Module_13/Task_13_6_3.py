# Задача 3. Число наоборот 2
# Что нужно сделать
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет каждое число
# на число, которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их, снова переворачивает и выводит ответ на экран.
# Пример:
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
# Сумма наоборот: 225

def reverse_num(num):
    num_str = str(num)
    reversed_num_str = num_str[::-1]
    reversed_num = int(reversed_num_str)
    return reversed_num


def sum_of_nums(a, b):
    summ = a + b
    return summ


n = int(input('Enter 1st num: '))
k = int(input('Enter 2nd num: '))
reversed_n = reverse_num(n)
reversed_k = reverse_num(k)

print(f'1st reversed num: {reversed_n}\n'
      f'2nd reversed num: {reversed_k}\n'
      f'Sum of nums: {sum_of_nums(n, k)}\n'
      f'Sum of reversed nums: {sum_of_nums(reversed_n, reversed_k)}')
