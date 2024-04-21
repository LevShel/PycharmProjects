# Задача 2. Однострочный код 2
# Пользователь вводит строку, состоящую из любых символов. Напишите код, который выводит на экран список
# этих символов, исключая цифры и буквы в верхнем регистре.
#
# Пример работы консоли:
# Введите строку: qWe456rtY
# ['q', 'e', 'r', 't']

from typing import List

sym_list: List[str] = [sym for sym in input('Enter string: ')]
print(list(filter(lambda sym: sym.islower(), sym_list)))

