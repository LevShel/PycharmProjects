# Задача 3. Палиндром: возвращение
# Что нужно сделать
# Есть множество встроенных и внешних библиотек для работы с данными в Python. С некоторыми из них вы уже работали.
# Например, с модулем collections, когда использовали специальный класс OrderedDict, с помощью которого делали
# упорядоченный словарь. В этой библиотеке есть и другие возможности, но их немного. Официальная документация:
# collections — Container datatypes.
# Используя модуль collections, реализуйте функцию can_be_poly, которая принимает на вход строку и проверяет,
# можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False

from collections import Counter


def can_be_poly(s: str) -> bool:
    # # Подсчет количества каждого символа в строке
    # counts = Counter(s)
    # # Подсчет количества символов с нечетным количеством вхождений
    # odd_counts = sum(1 for count in counts.values() if count % 2 != 0)
    # # Если количество символов с нечетным количеством вхождений не превышает одного,
    # # то из строки можно составить палиндром
    # return odd_counts <= 1
    return len(list(filter(lambda x: x % 2, Counter(s).values()))) <= 2


# Проверка
print(can_be_poly('abcba'))  # True
print(can_be_poly('abbbc'))  # False
