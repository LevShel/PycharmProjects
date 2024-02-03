# Задача 2. Дорога
# Мы делаем текстовую игру — гонку, и нам нужно вывести на экран что-то вроде трассы,
# где будут соревно-ваться наши машины. Напишите программу, которая выводит такую
# дорогу на экран (поле 20×50).

x = 20
y = 50

for row in range(x):
    for col in range(y):
        if row == x/2:
            print('-', end='')
        elif col == row + y/2 + 5:
            print('\\', end='')
        elif col == -row + x:
            print('/', end='')
        elif col == y/2:
            print('|', end='')
        else:
            print(' ', end='')
    print()