# Задача 3. Прятки 2
# Пока все прятались, “голя” решил схитрить и считать секунды быстрее, чем нужно.
# Напишите программу, которая выводит только чётные числа в порядке убывания
# от N до 1 включительно, используя цикл for. Нельзя использовать условный оператор.

import time

timer = int(input('Enter num of seconds: '))
timer = timer // 2
print()
for sec in range(timer, 0, -1):
    print(sec*2)
    time.sleep(1)
print('I go!')