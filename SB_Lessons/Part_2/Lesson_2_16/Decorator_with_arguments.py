import functools
import time
from typing import Callable, Any, Optional


def timer_with_precision(_func: Optional = None, *, precision: int = 10) -> Callable:
    """
    Декоратор декоратора, в котором есть
    аргумент "precision" для установки точности округления.
    По-умолчанию значение = 10,
    при указании декоратора над функцией - можно изменить значение по-умолчанию.
    """
    def timer_decorator(func: Callable) -> Callable:
        """
        Декоратор, выводящий время,
        которое заняло выполнение
        декорируемой функции.
        """
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            run_time = round(ended_at - started_at, precision)
            print(f'Function worked {run_time} sec.')
            return result
        return wrapped_func
    if _func is None:
        return timer_decorator
    return timer_decorator(_func)


@timer_with_precision
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов для каждого N от 0 до 10 000,
    где 0 <= N <= 100
    :return: сумма квадратов
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10 ** 4)])
    return result


@timer_with_precision(precision=2)
def cubes_sum(number: int) -> int:
    """
        Функция нахождения суммы кубов для каждого N от 0 до 10 000,
        где N задаётся пользователем при вызове функции
        :return: сумма кубов
    """
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10 ** 4)])
    return result


print(squares_sum.__name__, squares_sum.__doc__)
my_sum = squares_sum()
print('result =', my_sum)
print('\n')
print(cubes_sum.__name__, cubes_sum.__doc__)
my_cubes = cubes_sum(200)
print('result =', my_cubes)
