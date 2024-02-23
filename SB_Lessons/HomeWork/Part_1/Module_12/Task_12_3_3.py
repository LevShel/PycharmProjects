# Задача 3. Простые числа
# Пользователь вводит число N — количество чисел в последовательности.
# Напишите функцию isPrime, кото-рая проверяет, является ли число простым
# и выводит ответ в консоль.

def isPrime(num):
    if num % 1 == 0:
        print('Num is simple.')
    else:
        print('Num isn`t simple')

n = float(input('N = '))
isPrime(n)