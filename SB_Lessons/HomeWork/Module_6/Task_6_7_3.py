# Задача 3. Слишком большие числа
# Что нужно сделать
# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета,
# что числа не помещаются на бумаге.
# Напишите программу, которая считала бы для него, сколько цифр во вводимом числе.
# Обратите внимание, что число 0 имеет одну цифру.

num = int(input('Enter num: '))

i = 1

while num // 10 != 0:
    i += 1
    num = num // 10

print(f'There are {i} nums.')