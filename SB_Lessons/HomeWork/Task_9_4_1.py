# Задача 1. Доска
# Используя новые знания о циклах и операторе end, напишите программу,
# которая выводит на экрану вот такую «доску»:
# ------------
# |0000000000|
# |0000000000|
# |0000000000|
# |0000000000|
# ------------

def minuses():
    for sym in range(12):
        print('-', end='')
    print()

def zeroes():
    print('|', end='')
    for sym in range(10):
        print('0', end='')
    print('|')

minuses()
for row in range(4):
    zeroes()
minuses()