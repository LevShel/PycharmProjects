# Задача 3. Апгрейд калькулятора
# Что нужно сделать
# Степан использует калькулятор для расчёта суммы и разности чисел,
# но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал
# калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие, которое нужно
# сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.
# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума
# при помощи аргументов.

import math


def def_floor(num):  # Округление вниз
    print(f'⌊{num}⌋ = ', math.floor(num))


def def_ceil(num):  # Округление вверх
    print(f'⌈{num}⌉ = ', math.ceil(num))


def def_abs(num):  # Модуль числа
    print(f'|{num}| = ', math.fabs(num))


def def_sqrt(num):  # Квадратный корень
    print(f'√{num} = ', math.sqrt(num))


def def_exp(num):  # Экспонента в степени числа
    print(f'e^{num} = ', math.exp(num))


def def_log(num):  # Натуральный логарифм числа
    print(f'log({num}) = ', math.log(num))


def def_log2(num):  # Логарифм числа по основанию 2
    print(f'log2({num}) = ', math.log2(num))


def def_log10(num):  # Логарифм числа по основанию 10
    print(f'log10({num}) = ', math.log10(num))


def def_sin(num):  # Синус числа
    print(f'sin({num}) = ', math.sin(num))


def def_cos(num):  # Косинус числа
    print(f'cos({num}) = ', math.cos(num))


def def_factorial(num):  # Факториал (если введенное число было натуральным)
    if num % 1 == 0:
        num = int(num)
        print(f'{num}! = ', math.factorial(num))
    else:
        print(f'Число {num} не натуральное.')


while True:
    n = float(input('\n Enter num: '))
    action = input('Choose action:\n'
                   '1. Округление вниз\n'
                   '2. Округление вверх\n'
                   '3. Модуль числа\n'
                   '4. Квадратный корень\n'
                   '5. Экспонента в степени числа\n'
                   '6. Натуральный логарифм числа\n'
                   '7. Логарифм числа по основанию 2\n'
                   '8. Логарифм числа по основанию 10\n'
                   '9. Синус числа\n'
                   '10. Косинус числа\n'
                   '11. Факториал\n'
                   '    :> ')

    if action == '1':
        def_floor(n)
    elif action == '2':
        def_ceil(n)
    elif action == '3':
        def_abs(n)
    elif action == '4':
        def_sqrt(n)
    elif action == '5':
        def_exp(n)
    elif action == '6':
        def_log(n)
    elif action == '7':
        def_log2(n)
    elif action == '8':
        def_log10(n)
    elif action == '9':
        def_sin(n)
    elif action == '10':
        def_cos(n)
    elif action == '11':
        def_factorial(n)
