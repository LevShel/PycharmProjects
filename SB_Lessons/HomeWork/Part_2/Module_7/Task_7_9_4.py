# Задача 4. По парам
# Что нужно сделать
# Напишите программу, которая инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
# Дополнительно: решите задачу несколькими способами.
# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

import random

list_original = [random.randint(0, 10) for i in range(10)]
print(f'Original list:\n'
      f'{list_original}')

index = 0
list_new = []
while index != len(list_original):
    list_new.append((list_original[index], list_original[index + 1]))
    index += 2
print(f'New list:\n'
      f'{list_new}')
