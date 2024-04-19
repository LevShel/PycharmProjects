# Задача 1. Таймер
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера: функция должна работать с оператором with
# и замерять время работы вложенного кода.

import time
from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(time.time() - start)


with timer() as t1:
    print('Part 1')
    val_1 = 100 * 100 ** 1000000
    val_1 += 'qwerty'
    # some another code

with timer() as t2:
    print('Part 2')
    val_2 = 200 * 200 ** 2000000
    # some another code

with timer() as t3:
    print('Part 3')
    val_3 = 300 * 300 ** 3000000
    # some another code