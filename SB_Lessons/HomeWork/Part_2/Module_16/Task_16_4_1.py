# Задача 1. Createtime
# Реализуйте декоратор класса, который выдаёт дату и время создания, а также список всех методов объекта класса
# каждый раз, когда объект класса создаётся в основном коде.

import datetime
import functools
import time


# from datetime import datetime


def creation(cls):
    """ Декоратор класса, выводящий дату и время создания класса. """

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'The time when the instance of the class was created: {datetime.datetime.now(datetime.UTC)}')
        return instance

    return wrapper


def method_name(instance):
    """ Декоратор класса, выводящий список всех методов объекта класса. """
    print(f'Methods list of class {instance.__name__}:')
    for i_method_name in dir(instance):
        if not i_method_name.startswith('__'):
            print(i_method_name)
    return instance


@creation
@method_name
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

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
print('\n')
my_funcs_2 = Functions(max_num=2000)
time.sleep(1)
print('\n')
my_funcs_3 = Functions(max_num=3000)
