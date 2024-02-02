# Задание 3. Театр
# В городе планируют построить театр под открытым небом, но для начала нужно
# оценить, сколько сделать рядов, сидений в них и каким должно быть расстояние
# между рядами.
# Что нужно сделать
# Напишите программу, которая получает на вход количество рядов, сидений
# и свободных метров между ря-дами, а затем выводит примерный макет театра на экран.

def seats_in_row():
    for seat in range(seats):
        print('=', end='')
    print(' ', end='')


def space_in_row():
    for meter in range(space):
        print('*', end='')
    print(' ', end='')


rows = int(input('Enter num of rows: '))
seats = int(input('Enter num of seats: '))
space = int(input('Enter space in meters: '))

width = int((seats * 2) + space + 2)
print()
print('SCENE\n'.center(width))
for row in range(rows):
    seats_in_row()
    space_in_row()
    seats_in_row()
    print()