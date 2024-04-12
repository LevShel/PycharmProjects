# Задача 2. Таймер
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить скорость передачи данных
# на нескольких десятках сайтов. Конечно же, вручную «щёлкать» сайты и замерять время вам было лень, поэтому возникла
# идея написать «автотест», который всё сделает сам.
# С помощью понятия функции высшего порядка реализуйте функцию-таймер, которая замеряет время работы переданной
# функции func и выдаёт ответ на экран.
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.

import functools
import time
from typing import Callable, Any


def timer(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> str:
        started_at = time.time()
        func(*args, **kwargs)
        finished_at = time.time()
        run_time = round(finished_at - started_at, 2)
        return f'\nCompleted at {run_time} sec.'

    return wrapped_func


@timer
def print_nums(limit: int) -> Any:
    for i in range(limit + 1):
        print(i, end=' ')
        time.sleep(1)


print(print_nums(3))
