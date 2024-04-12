# Задача 2. Плагины
# Один проект состоит из огромного количества разнообразных функций, часть из которых используется в других проектах
# в качестве плагинов, то есть они как бы «подключаются» и создают дополнительный функционал.
# Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как плагины и заносить
# их в соответствующий словарь.

from typing import Callable

PLUGINS = dict()


def plugins_dict(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@plugins_dict
def say_hello() -> str:
    return 'Hello, World!'


@plugins_dict
def say_bye() -> str:
    return 'Goodbye!'


print(PLUGINS)
