# Задание 2. Лестница
# Что нужно сделать
# Напишите программу, которая выводит «лестницу» из чисел, когда пользователь вводит число N:
# Enter num: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = 5

for row in range(n):
    for col in range(n):
        if row == col:
            print(row+1, end='\t')
        elif row > col:
            print(row+1, end='\t')
    print()