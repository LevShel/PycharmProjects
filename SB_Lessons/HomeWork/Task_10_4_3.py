# Задача 3. Лестница чисел
# Пользователь вводит число N. Напишите программу, которая по этому числу выводит
# вот такую лестницу из чисел:
# 0 1 2 3 4 5
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

n = int(input('Enter size: '))

for row in range(n+1):
    for col in range(n+1):
        if row == col:
            print(col, end=' ')
        elif row < col:
            print(col, end=' ')
    print()