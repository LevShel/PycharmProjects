# Задача 3. Различные цифры
# Напишите программу, которая находит все различные цифры в символьной строке.
# Для решения используйте множество (цифры будут различные, и поиск во множестве намного
# быстрее, чем в списке).
#
# Пример:
# Введите строку: ab1n32kz2
# Различные цифры строки: 123

str_text = input('>: ')
set_text = set(str_text)
set_nums = set()
for sym in set_text:
    # if '0' <= sym <= '9':
    if sym.isdigit():
        set_nums.update(sym)
print('Nums in string: ', end='')
print(', '.join(sorted(set_nums)))