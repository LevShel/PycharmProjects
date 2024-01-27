import random

# Исходный список из 10 рандомных числе от 1 до 4
numbers_list = [random.randint(1, 4) for _ in range(10)]
print('Random nums list: ', numbers_list)

# Длинный способ создания списка уникальных значений
new_list = []
for i_num in numbers_list:
    if i_num not in new_list:
        new_list.append(i_num)
print('Not-repeated num: ', sorted(new_list))

# Быстрый способ уникальных значений
unique = set(numbers_list)
print('Not-repeated num: ', unique)