# Задача 1. Координаты точки
# Лена пишет программу для построения графиков функций, чтобы можно было анализировать
# статистику посещений её сайта. Перед тем как построить график функции,
# Лена сначала расставляет на нём точки. У каждой точки есть координаты: X и Y.
# Лене также нужно найти сумму этих координат, чтобы убедиться в их правильном расположении.
#
# •	Реализуйте программу, которую мы разбирали в уроке: она запрашивает у пользователя
# два числа и выводит их сумму на экран.
# •	Используйте функцию int() для преобразования входящих данных из текста в число.
# Для этого внутри скобок функции int вставьте команду input. Результат должен быть таким:
#

x = int(input('x = '))
y = int(input('y = '))

sum = x + y
print('x + y =', sum)