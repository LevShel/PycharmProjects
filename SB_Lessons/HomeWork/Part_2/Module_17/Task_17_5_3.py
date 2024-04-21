# Задача 3. Функция reduce
# Помимо map и filter, есть ещё одна функция — reduce. Она применяет указанную функцию
# к элементам последовательности, сводя её к единственному значению. Однако используют reduce довольно редко.
# Начиная с третьей версии Python, эту функцию даже вынесли из встроенных функций в модуль functools.
#
# Пример кода с reduce:
# from functools import reduce
# from typing import List
#
#
# def my_add(a: int, b: int) -> int:
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result
#
#
# numbers: List[int] = [0, 1, 2, 3, 4]
# print(reduce(my_add, numbers))
#
# Результат:
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10
#
# Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке:
#

from functools import reduce

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]

""" CLASSIC """
count: int = 0
for text in sentences:
    if 'was' in text:
        count += 1
print("Количество вхождений слова 'was':", count)

""" REDUCE """
count_was: int = reduce(lambda acc, sentence: acc + sentence.count("was"), sentences, 0)
print("Количество вхождений слова 'was':", count_was)
