# Задача 3. Координатные оси
# Напишите программу, которая рисует координатные оси на поле 20×50.

x = 50
y = 20

for sym in range(y//2):
    print(' '*(x//2-1), '|')

for sym in range(x//2):
    print('-', end='')

print('+', end='')

for sym in range(x//2):
    print('-', end='')
print()

for sym in range(y//2):
    print(' '*(x//2-1), '|')