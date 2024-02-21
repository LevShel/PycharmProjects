# Задача 6. НОД
# Что нужно сделать
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a = int(input('a = '))  # 140
b = int(input('b = '))  # 96

# num = a // b                    # 140:96=1 (44)
# remains = a % b                 # 44
# gcd = remains
#
# num = b // remains              # 96:44=2 (8)
# remains2 = b % remains          # 8
# gcd = remains2
#
# num = remains // remains2       # 44:8=5 (4)
# remains = remains % remains2   # 4
# gcd = remains
#
# num = remains // remains2       # 8:4=2 (0)
# remains2 = remains % remains2   # 0
# gcd = remains2

result = gcd(a, b)
print(f"Наибольший общий делитель чисел {a} и {b} равен {result}.")
