# Задание 7. Три списка
# Что нужно сделать
# Даны три списка.
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Нужно выполнить две задачи:
# 1.	найти элементы, которые есть в каждом списке;
# 2.	найти элементы из первого списка, которых нет во втором и третьем списках.
# Каждую задачу нужно выполнить двумя способами:
# 1.	без использования множеств;
# 2.	с использованием множеств.
# Пример выполнения на других данных:
# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]
# Вывод:
# Задача 1:
# Решение без множеств: 2
# Решение с множествами: 2
# Задача 2:
# Решение без множеств: 1
# Решение с множествами: 1

print('\n\tTask 1:')

print('Solution without sets:', end=' ')
list_nums = []
list_nums.extend(array_1)
list_nums.extend(array_2)
list_nums.extend(array_3)
list_nums_each = []
for num in list_nums:
    i = list_nums.count(num)
    if i == 3:
        if num not in list_nums_each:
            list_nums_each.append(num)
print(' '.join(map(str, sorted(list_nums_each))))

print('Solution with sets:', ' '.join(map(str, sorted(set(array_1) & set(array_2) & set(array_3)))))

print('\n\tTask 2:')

print('Solution without sets:', end=' ')
for num in sorted(array_1):
    if num not in array_2 and num not in array_3:
        print(num, end=' ')

print('\nSolution with sets:', ' '.join(map(str, sorted((set(array_1)).difference(set(array_2), set(array_3))))))