# Задача 1. Врата
# Напишите программу, которая выводит в консоль «врата», состоящие из тире,
# вертикальных линий и про-белов. Поле состоит из 20 строк и 30 столбцов
# (но не стесняйтесь пробовать и другие размеры).

x = 30
y = 20

for sym in range(x):
    print('-', end='')
print()
for sym in range(y):
    print('|' + ' '*(x-2) + '|')