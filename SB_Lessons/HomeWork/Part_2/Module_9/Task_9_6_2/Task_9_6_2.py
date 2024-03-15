# Задача 2. Дзен Пайтона
# Что нужно сделать
# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии программирования
# на языке Python. Выглядит он так:
# Beautiful is better than ugly.
# ...
# Namespaces are one honking great idea -- let's do more of those!
#
# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду import this.
# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# ...

file = open('zen.txt', 'r')
text = [i_str for i_str in file]
file.close()

for j_str in text[::-1]:
    print(j_str, end='')