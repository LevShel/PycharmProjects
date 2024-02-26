# Задача 2. «Назад в будущее»
# Вы — один из разработчиков языка программирования Python, и вы пишете
# специальный математический модуль, который можно было бы просто подключить
# внутри программы и облегчить жизнь всем программистам.
# Реализуйте функцию gcd, которая получает два параметра — два числа —
# и возвращает наибольший общий делитель этих двух чисел.
# Пример работы программы:
# Введите первое число: 6
# Введите второе число: 10
# НОД = 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a = int(input('a = '))
b = int(input('b = '))

result = gcd(a, b)
print(f"Наибольший общий делитель чисел {a} и {b} равен {result}.")