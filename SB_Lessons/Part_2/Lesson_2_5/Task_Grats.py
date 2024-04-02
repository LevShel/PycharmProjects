list_names = []
while True:
    name = input('Enter name: ')
    if name == 'end':
        break
    list_names.append(name)

for name in list_names:
    grats_message = f'\nCongratulation, {name}!'
    print(grats_message)