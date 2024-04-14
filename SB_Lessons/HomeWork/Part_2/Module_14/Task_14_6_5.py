# Задача 5. Кэширование для ускорения вычислений
# Контекст
# Вы разрабатываете программу для оптимизации вычислений чисел Фибоначчи. Числа Фибоначчи вычисляются рекурсивной
# функцией, каждое число равно сумме двух предыдущих чисел. Однако вы заметили, что при больших значениях чисел
# Фибоначчи вычисления занимают значительное время, так как многие значения вычисляются повторно. Вам поручено создать
# декоратор, который кэширует результаты вызова функции и позволяет избежать повторных вычислений для одних и тех же
# аргументов.
# Задача
# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования) результаты вызова функции
# и, при повторном вызове с теми же аргументами, возвращает сохранённый результат.
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и, если такие аргументы уже
# использовались, должен вернуть сохранённый результат вместо запуска расчёта.

import functools
import time
from typing import Callable, Any


def cache(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped(*args) -> Any:
        if not hasattr(wrapped, 'cache_list'):
            wrapped.cache_list = []
        for value in func(*args):
            wrapped.cache_list.append(value)
        print(wrapped.cache_list)
        return func(*args)

    return wrapped


@cache
def fibonacci(number: int) -> Any:
    current_value = 0
    next_value = 1
    for _ in range(number):
        yield current_value
        current_value, next_value = next_value, current_value + next_value


fib_seq = fibonacci(10)
for i_value in fib_seq:
    print(i_value)
    time.sleep(1)
