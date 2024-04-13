# Задача 4. Счётчик
# Что нужно сделать
# Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).

import functools
import time
from typing import Callable, Any


# def counter(func: Callable) -> Any:
#     __count = 0
#
#     def get_count() -> int:
#         return __count
#
#     def set_count(new_count: int) -> int:
#         __count = new_count
#         return __count
#
#     @functools.wraps(func)
#     def wrapping(*args, **kwargs) -> None:
#         func(*args, **kwargs)
#         i = get_count()
#         i += 1
#         print(i)
#         set_count(i)
#
#     return wrapping

def counter(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        if not hasattr(wrapped, 'call_count'):
            wrapped.call_count = 0
        wrapped.call_count += 1
        print(wrapped.call_count)
        return func(*args, **kwargs)

    return wrapped


@counter
def test() -> None:
    """
    Какая-то тестовая функция, в которой ничего не происходит,
    а на экран выводится сообщение о том, что "тут что-то происходит".
    """
    print('<Тут что-то происходит...>')


""" Основной код программы. """
print('\n\tStart:\n')
test()  # counter = 1
time.sleep(3)
test()  # counter = 2
time.sleep(3)
test()  # counter = 3
print('\n\tFinished.')
