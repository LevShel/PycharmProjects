# Задача 2. Директории
# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и временно меняет текущую рабочую
# директорию на новую. Функция должна быть контекст-менеджером. Также реализуйте обработку ошибок (например,
# если такого пути не существует). Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться
# в изначальную рабочую директорию.
#
# Пример основного кода:
# with in_dir('C:\\'):
#     print(os.listdir())
# Результат:
# <тут содержимое папки C:\\>

import os
from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def in_dir(new_path) -> Iterator:
    try:
        # os.chdir(new_path)
        yield os.chdir(new_path)
    except Exception as exc:
        print(exc)
        return True


with in_dir('E:\\'):
    print(os.listdir())
