def rover_move(size_x, size_y, x, y, move):
    # move = input(f'The rover is at position [{x}, {y}]\n'
    #              'enter the command: ').upper()
    if move == 'W' and (0 <= y < size_y):
        y += 1
    elif move == 'A' and (0 < x <= size_x):
        x -= 1
    elif move == 'S' and (0 < y <= size_y):
        y -= 1
    elif move == 'D' and (0 <= x < size_x):
        x += 1
    return x, y


size_x = 15
size_y = 20

x = 8
y = 10

for sym in range(size_x):
    print('+', end=' ')
print()
for sym in range(size_y-2):
    print('+', ' '*(size_x*2-5), '+')
for sym in range(size_x):
    print('+', end=' ')

# while True:
#     move = input(f'The rover is at position [{x}, {y}]\n'
#                  'enter the command: ').upper()
#     x, y = rover_move(size_x, size_y, x, y, move)