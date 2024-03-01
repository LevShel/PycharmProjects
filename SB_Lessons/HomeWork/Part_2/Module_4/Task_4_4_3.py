# Задача 3. Удаление части
# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B).
# Напишите программу, которая удаляет элементы списка с индексами от А до В. Не используйте
# дополнительные переменные и методы списков.
import random

original_list = [random.randint(0, 10) for num in range(10)]
print(f'{original_list}')
a = int(input('a = '))
b = int(input('b = '))
print(original_list[:a:]+original_list[b::])