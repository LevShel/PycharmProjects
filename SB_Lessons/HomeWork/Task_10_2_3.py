# Задача 3. Координатные оси
# Напишите программу, которая рисует координатные оси на поле 20×50.

# for sym in range(20):
#     print('+', end=' ')
# print()
x = 10
y = 6

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