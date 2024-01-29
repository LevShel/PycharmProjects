# Задача 6. Проверяем бухгалтера
# Что нужно сделать
# Невнимательный бухгалтер Антон складывает числа быстро,
# но иногда забывает о двух последних разрядах. Чтобы помочь Антону,
# напишите программу, которая бы складывала только два последних разряда.
# Реализуйте программу, которая запрашивает два числа у пользователя.
# После этого у каждого числа возь-мите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.
# Пример:
#

first_num = int(input('Enter first num: '))
second_num = int(input('Enter second num: '))

sum = first_num % 100 + second_num % 100

print('\n', sum)