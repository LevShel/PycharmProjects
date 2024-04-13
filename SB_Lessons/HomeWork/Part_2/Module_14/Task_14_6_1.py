# Задача 1. Как дела?
# Что нужно сделать
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он написал надоедливый декоратор, который
# при вызове декорируемой функции спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то вроде
# «А у меня не очень!» и только потом запускает саму функцию. Правда, после такой выходки Васю чуть не уволили с работы.
# Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.
# Пример кода:
# @how_are_you
# def test():
#     print('<Тут что-то происходит...>')
#
#
# test()
# Результат:
# Как дела? Хорошо.
# А у меня не очень! Ладно, держи свою функцию.
# <Тут что-то происходит...>

import functools
import time
from typing import Callable, Any


def how_are_you(func: Callable) -> Any:
    """Надоедливый декоратор"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print('\nКак дела?')
        input('>: ')
        print('А у меня не очень!')
        time.sleep(1)
        print('Ладно, держи свою функцию.\n')
        time.sleep(1)
        func(*args, **kwargs)

    return wrapper


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def say_hello() -> None:
    print('Hello, World!')


@how_are_you
def say_bye() -> None:
    print('Goodbye!')


test()
say_hello()
say_bye()
