# Задача 8. По желанию. Обмен значений двух переменных
# Что нужно сделать
# Дана программа, которая запрашивает у пользователя два слова,
# а затем выводит их на экран два раза. Ско-пируйте эту программу в редактор и проверьте.
#
# a = input('Введите первое слово: ')
# b = input('Введите второе слово: ')
# print(a, b)
# # стереть эту строчку и вставить свой код здесь
# print(a, b)
#
# Задача: поменять значения переменных a и b местами. Изменять, удалять,
# менять местами 1-ю, 2-ю, 3-ю и последнюю строчки нельзя.
# Но в 4-ю строку можно вставлять сколько угодно кода, не трогая последний принт.
# Пример результата работы программы:
#
#
# Что оценивается
# Результат вычислений и вывода корректен. Строки с print остались неизменными,
# не изменён порядок вывода переменных.
#
# Что оценивается (общее)
# •	Правильно оформленный input, без пустого приветствия для ввода (видео 2.3).
# •	Переменные имеют значащие имена, не только a, b, c, d (видео 2.3).
# •	Пробелы после запятых, пробелы при бинарных операциях.
# •	Отсутствие пробелов после имён функций и перед скобками:
# “print ()”,“input ()” — неверно, “print()” — верно.

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
temp = a
a = b
b = temp
print(a, b)