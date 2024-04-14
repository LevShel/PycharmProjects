import functools
from collections.abc import Callable


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('Function {func} was run: {count} times.'.format(
            func=func.__name__, count=wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@counter
def test():
    print('test')


test()
test()
test()
