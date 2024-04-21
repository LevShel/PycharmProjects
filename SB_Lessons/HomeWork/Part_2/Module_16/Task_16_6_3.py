# Задача 3. Логирование в формате
# Что нужно сделать
# Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов)
# и в который можно передавать формат вывода даты и времени логирования.
# Пример кода, передаётся формат «месяц день год — часы:минуты:секунды»:
# @log_methods("b d Y — H:M:S")
# class A:
#     def test_sum_1(self) -> int:
#         print('test sum 1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# @log_methods("b d Y - H:M:S")
# class B(A):
#     def test_sum_1(self):
#         super().test_sum_1()
#         print("Наследник test sum 1")
#
#
#     def test_sum_2(self):
#         print("test sum 2")
#         number = 200
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# my_obj = B()
# my_obj.test_sum_1()
# my_obj.test_sum_2()
# Результат:
# Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_1.
# Завершение 'A.test_sum_1', время работы = 0,187 s.
# Тут метод test_sum_1 у наследника.
# Завершение 'B.test_sum_1', время работы = 0,187 s.
# Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_2 у наследника.
# Завершение 'B.test_sum_2', время работы = 0,370 s.
import datetime
import functools
# from datetime import datetime
from typing import Callable, Any


def log_methods(datetime_format: str) -> Callable:
    def wrapper(cls: type) -> type:
        class Wrapped(cls):
            def __getattribute__(self, name) -> Any:
                attr = super().__getattribute__(name)
                if not callable(attr) or name.startswith("__"):
                    return attr

                @functools.wraps(attr)
                def wrapped(*args, **kwargs) -> Callable:
                    start_time = datetime.datetime.now()
                    print(
                        f"Запускается '{cls.__name__}.{name}'. Дата и время запуска: {start_time.strftime(datetime_format)}.")
                    result = attr(*args, **kwargs)
                    end_time = datetime.datetime.now()
                    print(
                        f"Завершение '{cls.__name__}.{name}', время работы = {(end_time - start_time).total_seconds()} s.")
                    return result

                return wrapped

        return Wrapped

    return wrapper


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
