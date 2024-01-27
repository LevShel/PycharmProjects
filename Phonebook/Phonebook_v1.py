# Шапка
name_of_programm = 'PhoneBook'
print('+', '-'*(len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-'*(len(name_of_programm)-8), 'by ШелЛ +\n')

phonebook_dict = {
    'ShelL': 89854239970,
    'Kras': 89777072380,
    'Tosha': 89260642472,
    'Den': 89251356664
}

# Описание комманд
command = ''
# Меню
def phonebook_menu():
  print('\nM E N U\nYou can use:\nA. Add\nS. Search\nC. Change\nV. View all\nD. Delete\nQ: Quit\n')

# Цикл программы
while True:
    phonebook_menu()
    command = input("Select an action: ").upper()

# Добавление контакта
    if command == 'A':
        name = input('\nEnter name: ')
        phone = input('Enter phone: ')
        phonebook_dict[name] = phone
        print('\nOk. {name} with phone {phone} was added in phonebook.'.format(name=name, phone=phone))

# Поиск контакта
    if command == 'S':
        name = input('\nEnter name: ')
        if name in phonebook_dict:
            print('\n{name}'.format(name=name), phonebook_dict[name])
        else:
            print('\n{name} does not exist.'.format(name=name))

# Изменение контакта
    if command == 'C':
        name = input('\nEnter name: ')
        if name in phonebook_dict:
            print('What change in {name}'.format(name=name), phonebook_dict[name], ' ?')
            answer = input('Press N for update name or T for update telephone number: ').upper()
            if answer == 'N':
                new_name = input('Enter new name: ')
                phonebook_dict[new_name] = phonebook_dict.pop(name)
                print('\nOk. Contact {name} was renamed to {new_name}.'.format(name=name, new_name=new_name))
            else:
                print('\n{name}'.format(name=name), phonebook_dict[name])
                phone = input('New phone number: ')
                phonebook_dict[name] = phone
                print('\nOk. New phone number {phone} for {name} was added in phonebook.'.format(name=name, phone=phone))
        else:
            print('\n{name} does not exist.'.format(name=name))

# Отображение всех контактов
    if command == 'V':
        print('\nContacts in phonebook:')
        for contact in sorted(phonebook_dict.keys()):
            print(contact, end=' ')
            print(phonebook_dict[contact])

# Удаление контакте
    if command == 'D':
        name = input('\nEnter name: ')
        if name in phonebook_dict:
            print('Delete ',phonebook_dict[name], ' ?')
            answer = input('Press Y or N: ').upper()
            if answer == 'Y':
                del phonebook_dict[name]
                print('\nOk. Contact {name} was deleted from phonebook.'.format(name=name))
            else:
                print('\nCanceled.')
        else:
            print('\n{name} does not exist.'.format(name=name))

# Завершение работы
    if command == 'Q':
        print('\nThe work with the phonebook is completed! To close the window, press any key.\n')
        print('~~~~~~~~~~~~')
        input()
        break