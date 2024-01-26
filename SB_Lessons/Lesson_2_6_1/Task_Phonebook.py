phonebook_dict = {
    'ShelL': 89854239970,
    'Kras': 89777072380,
    'Tosha': 89260642472,
    'Den': 89251356664
}
while True:
    name = input('Enter name: ')

    if name in phonebook_dict:
        print('{}'.format(name), phonebook_dict[name])
    else:
        print('{} does not exist.'.format(name))