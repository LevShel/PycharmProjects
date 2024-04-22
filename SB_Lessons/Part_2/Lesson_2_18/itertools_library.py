import itertools

colors = ['red', 'blue', 'green', 'yellow']

for item in itertools.permutations(colors, 4):
    print(item)

print('=' * 40)

for item in itertools.combinations(colors, 2):
    print(item)

print('=' * 40)

my_cycle = itertools.cycle(colors)
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
