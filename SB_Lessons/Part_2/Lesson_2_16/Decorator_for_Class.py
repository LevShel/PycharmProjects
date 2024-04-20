# from datetime import datetime
import datetime
import functools
import time
from typing import Callable


def creation_time(cls):
    """ Декоратор класса, выводящий дату и время создания класса. """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'The time when the instance of the class was created: {datetime.datetime.now(datetime.UTC)}')
        return instance
    return wrapper


def timer(func: Callable) -> Callable:
    """ Декоратор класса, выводящий время, которое заняло выполнение декорируемой функции или метода. """
    def wrapped_func(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 2)
        print(f'Function worked {run_time} sec.')
        return result
    return wrapped_func


def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его ко всем методам класса.
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if not i_method_name.startswith('__'):
                current_method = getattr(cls, i_method_name)
                decorated_method = decorator(current_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@creation_time
@for_all_methods(timer)
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    # @timer
    def squares_sum(self) -> int:
        """
        Функция нахождения суммы квадратов для каждого N от 0 до max_num,
        где 0 <= N <= 100
        :return: сумма квадратов
        """
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_num)])
        return result

    # @timer
    def cubes_sum(self, number: int) -> int:
        """
            Функция нахождения суммы кубов для каждого N от 0 до max_num,
            где N задаётся пользователем при вызове функции
            :return: сумма кубов
        """
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])
        return result


my_funcs_1 = Functions(max_num=1000)
time.sleep(1)
my_funcs_2 = Functions(max_num=2000)
time.sleep(1)
my_funcs_3 = Functions(max_num=3000)
time.sleep(1)
my_funcs_1.squares_sum()
my_funcs_1.cubes_sum(number=10000)
