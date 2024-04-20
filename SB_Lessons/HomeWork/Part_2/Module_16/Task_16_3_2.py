# Задача 2. Замедление кода 2
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор, который перед выполнением
# декорируемой функции ждёт несколько секунд.
# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
# По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор можно было использовать
# как с аргументами, так и без них.

import functools
import time
from typing import Callable, Any, Optional


def slow_down(_func: Optional[Callable] = None, *, duration: int = 0):
    @functools.wraps(_func)
    def wrapped(func: Callable) -> Any:
        print(f'Start timer.sleep({duration})')
        time.sleep(duration)
        return func
    return wrapped


@slow_down(duration=3)
def any_func() -> None:
    return print('There`s something going on here...')


any_func()

