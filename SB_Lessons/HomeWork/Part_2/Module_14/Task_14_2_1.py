# Задача 1. Функции
# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
#
# def func_1(x):
#     return x + 10
#
# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов переданной функции.
# Пример основного кода:
# print(func_2(func_1, 9))
#
# Результат: 361.

from typing import Callable, Any


def func_1(x):
    return x + 10


def func_2(func: Callable, *args) -> Any:
    result = func(*args) * func(*args)
    return result


print((func_2(func_1, 9)))
