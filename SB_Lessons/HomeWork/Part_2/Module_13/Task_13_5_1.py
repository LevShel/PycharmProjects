# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор,
# который также в цикле будет бесконечно выдавать значения.
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

import time
from typing import Any


def infinite_numbers() -> Any:
    num = 1
    while True:
        yield num
        num += 1


my_gen = infinite_numbers()
for i_num in my_gen:
    print(i_num, end=' ')
    time.sleep(1)
