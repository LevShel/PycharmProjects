# Задача 5. Функция сортировки
# Что нужно сделать
# Напишите функцию, которая сортирует по возрастанию кортеж, состоящий из целых чисел,
# и возвращает его отсортированным. Если хотя бы один элемент не является целым числом,
# то функция возвращает исходный кортеж.
# Основной код оставьте пустым или закомментированным (используйте его только
# для тестирования).
# Пример вызова функции:
# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)

import random


def i_is_int(tpl):
    for i in tpl:
        if isinstance(i, int):
            continue
        elif isinstance(i, float) and i.is_integer():
            continue
        else:
            return False
    return True


tuple_original = (42, 23, 16, 15, 8, 4)
print(tuple_original)

if i_is_int(tuple_original):
    print(tuple(sorted(tuple_original)))
else:
    print(tuple_original)