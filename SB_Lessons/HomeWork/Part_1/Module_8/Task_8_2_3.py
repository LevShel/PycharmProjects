# Задача 3. Квадраты нечётных чисел
# Вводится число N. Напишите программу, которая выводит
# квадраты нечетных чисел от 1 до N. Нельзя ис-пользовать
# условные операторы. Можно использовать цикл while,
# но постарайтесь всё-таки решить с по-мощью конструкции for in range.
# Не нужно искать решение в интернете, попробуйте подумать сами,
# в сле-дующем уроке мы обязательно разберём эту задачу.

n = int(input('Even nums from1 to '))
for number in range(1, n+1, 2):
    print(f'{number}^2 = {number ** 2}')