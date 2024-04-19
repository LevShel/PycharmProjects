# Задача 1. Повторение кода
# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.

import functools
from typing import Callable, Any, Optional


def repeat(_func: Optional[Callable] = None, *, num: int = 1) -> Callable:
    if _func is None:
        return functools.partial(repeat, num=num)

    @functools.wraps(_func)
    def wrapped(*args, **kwargs) -> Any:
        result = None
        for _ in range(num):
            result = _func(*args, **kwargs)
        return result

    return wrapped


@repeat
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
