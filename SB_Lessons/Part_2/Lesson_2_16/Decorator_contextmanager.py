# """
# Task # 1
# """
# from collections.abc import Iterator
# from contextlib import contextmanager
#
#
# @contextmanager
# def next_num(num: int) -> Iterator[int]:
#     print('Входим в функцию')
#     try:
#         yield num + 1
#     except ZeroDivisionError as exc:
#         print(f'Обнаружена ошибка : {exc}')
#     finally:
#         print('Здесь код выполнится в любом случае')
#     print('Выход из функции')
#
#
# with next_num(-1) as some_next:
#     print(f'Следующее число = {some_next}')
#     print(10 / some_next)


"""
Task # 2
"""
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
