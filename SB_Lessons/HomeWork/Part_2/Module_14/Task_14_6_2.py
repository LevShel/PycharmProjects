# Задача 2. Замедление кода
# Что нужно сделать
# В программировании иногда возникает ситуация, когда работу функции нужно замедлить. Типичный пример — функция,
# которая постоянно проверяет, изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

import functools
import time
from typing import Callable, Any


def waiting(func: Callable) -> Any:
    """Декоратор, который перед выполнением декорируемой функции ждёт несколько секунд"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print('\nWait, please...\n')
        time.sleep(5)
        func(*args, **kwargs)

    return wrapper


@waiting
def test() -> None:
    print('<Тут что-то происходит...>')


test()
