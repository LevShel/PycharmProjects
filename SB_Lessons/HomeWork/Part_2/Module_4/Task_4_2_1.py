# Задача 1. Кубы и квадраты
# Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка:
# в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел
# в этом же диапазоне. Выведите списки на экран.
# Для генерации используйте list comprehensions (как и в следующих задачах).
#
# Пример:
# Левая граница: 5
# Правая граница: 10
#
# Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
# Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]

left_side = int(input('Left side: '))
right_side = int(input('Right side: '))
# new_list = [выражение for элемент in итерируемый_объект if условие]
cubes = [x**3 for x in range(left_side, right_side+1)]
squares = [x**2 for x in range(left_side, right_side+1)]
print(f'Cubes in range from {left_side} to {right_side}: {cubes}\n'
      f'Squares in range from {left_side} to {right_side}: {squares}.')