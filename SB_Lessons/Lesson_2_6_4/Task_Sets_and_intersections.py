nums_1 = {1, 2, 3, 4, 5}
nums_2 = {4, 5, 6, 7, 8}

# Одинаковые значения в обоих множествах (пересечение множеств)
print(nums_1.intersection(nums_2)) # вариант 1
print(nums_1 & nums_2) # вариант 2

# Объединение значений в обоих множествах
print(nums_1.union(nums_2)) # вариант 1
print(nums_1 | nums_2) # вариант 2

# Неповторяющиеся значения в множествах
print(nums_1.difference(nums_2)) # вариант 1
print(nums_1 - nums_2) # вариант 2
print(nums_2 - nums_1) # вариант 3