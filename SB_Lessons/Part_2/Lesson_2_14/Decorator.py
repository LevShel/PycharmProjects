import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """ Декоратор, выводящий время, которое заняло выполнение декорируемой функции. """

    def wrapped_func(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 2)
        print(f'Function worked {run_time} sec.')
        return result

    return wrapped_func


@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10 ** 4)])
    return result


@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10 ** 4)])
    return result


my_sum = squares_sum()
print(my_sum)

my_cubes = cubes_sum(200)
print(my_cubes)
