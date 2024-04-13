# Задача 3. Логирование
# Что нужно сделать
# Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции
# и её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log
# записываются название функции и ошибки.
# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки, а обрабатывала
# все декорируемые функции и сразу записывала все ошибки в файл.
# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.

import datetime
import functools
import time
from typing import Callable, Any


def logging(func: Callable) -> Any:
    """
    Декоратор logging, который будет отвечать за логирование функций
    """

    @functools.wraps(func)
    def wrapping(*args, **kwargs) -> Any:
        """
        В файл "function_errors.log" записываются:
         datetime.datetime.now(): текущие дата/время
         func.__name__: название функции
         func.__doc__: описание функции
         и ошибки, в случае их возникновения
        """
        with open('function_errors.log', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.datetime.now()}:\t{str(func.__name__)}\t{str(func.__doc__)}\n')
            try:
                func(*args, **kwargs)
            except Exception as e:
                file.write(f'\t{str(e)}\n\n')

    return wrapping


@logging
def test() -> None:
    """
    Какая-то тестовая функция, в которой ничего не происходит,
    а на экран выводится сообщение о том, что "тут что-то происходит".
    """
    print('<Тут что-то происходит...>')


@logging
def test_with_error() -> None:
    """
    Какая-то тестовая функция, в которой запрашивается ввод любой цифры.
    """
    inp_var = int(input('Print any digit: '))


""" Основной код программы. """
print('\n\tStart:\n')
test()
time.sleep(3)
test_with_error()
time.sleep(3)
test()
print('\n\tFinished.')
