# Задача 2. Соседи
# Дана строка S и номер позиции символа в строке. Напишите программу, которая выводит
# соседей этого символа и сообщение о количестве таких же символов среди этих соседей:
# их нет, есть ровно один или есть два таких же.
#
# Пример 1:
# Введите строку: abbc
# Номер символа: 3
#
# Символ слева: b
# Символ справа: c
#
# Есть ровно один такой же символ.
#
# Пример 2:
# Введите строку: abсd
# Номер символа: 3
#
# Символ слева: b
# Символ справа: d
#
# Таких же символов нет.

input_str = input('Введите строку: ')
sym_num = int(input('Номер символа: '))
print('Символ: ', input_str[sym_num - 1])
print('Символ слева: ', input_str[sym_num - 2])
print('Символ справа: ', input_str[sym_num])
same_sym = 0
if input_str[sym_num - 1] == input_str[sym_num - 2]:
    same_sym += 1
elif input_str[sym_num - 1] == input_str[sym_num]:
    same_sym += 1
print(f'Есть {same_sym} такой же символ.')