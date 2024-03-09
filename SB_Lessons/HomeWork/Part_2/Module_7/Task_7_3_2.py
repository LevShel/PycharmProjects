# Задача 2. Словари из списков
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита
# (могут повторяться). Затем для каждого списка создайте словарь из пар
# «индекс — значение» и выведите оба словаря на экран.
# Подсказка: random
#
# Пример:
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
#
# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т',
#                   7: 'ж', 8: 'е', 9: 'к'}
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р',
#                   7: 'б', 8: 'й', 9: 'р'}

import random
import string

list_1 = [random.choice(string.ascii_letters.lower()) for letter_1 in range(10)]
list_2 = [random.choice(string.ascii_letters.lower()) for letter_2 in range(10)]

dict_1 = {index: sym_1 for index, sym_1 in enumerate(list_1)}
dict_2 = {index: sym_2 for index, sym_2 in enumerate(list_1)}

print(f'1st list: {list_1}\n'
      f'2nd list: {list_2}\n'
      f'\n'
      f'1st dictionary: {dict_1}\n'
      f'2nd dictionary: {dict_2}')
