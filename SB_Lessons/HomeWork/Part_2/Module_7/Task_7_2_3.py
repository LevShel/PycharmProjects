# Задача 3. Неправильный код
# Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
# Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный
# индекс и случайное значение, а затем по этим индексу и значению меняет сам кортеж.
# Функция должна возвращать кортеж и случайное значение.
# В основном коде функция используется два раза, и на экран два раза выводится новый кортеж
# и случайное значение. Причём второй раз выводится сумма первого случайного значения
# и второго.
# Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.
#
# import random
#
# def change(nums):
#     index = random.randint(1, 5)
#     value = random.randint(100, 1000)
#     nums[index] = value
#     return nums, value
#
# my_nums = 1, 2, 3, 4, 5
#
# new_nums, rand_val = change(my_nums)
# print(new_nums, rand_val)
# new_nums = change(new_nums)
# rand_val += change(new_nums)
# print(new_nums, rand_val)

import random


def change(nums):
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    tuple_new_nums = tuple(nums[:index]) + (value,) + tuple(nums[index + 1:])
    return tuple_new_nums, value


tuple_nums = (1, 2, 3, 4, 5)
tuple_new_1, rand_val_1 = change(tuple_nums)
print(tuple_new_1, rand_val_1)
tuple_new_2, rand_val_2 = change(tuple_new_1)
print(tuple_new_2, rand_val_1 + rand_val_2)
