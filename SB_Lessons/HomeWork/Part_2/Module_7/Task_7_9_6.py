# Задача 6. Контакты — 3
# Что нужно сделать
# Мы уже помогали Степану с реализацией телефонной книги на устройстве, однако внезапно
# оказалось, что ей не хватает ещё одной полезной функции — поиска.
# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое
# он хочет совершить: добавить контакт или найти человека в списке контактов по фамилии.
# Действие «добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер
# телефона, добавляет их в словарь и выводит на экран текущий словарь контактов.
# Если этот человек уже есть в словаре, то выводится соответствующее сообщение.
# Действие «поиск человека по фамилии»: программа запрашивает фамилию и выводит
# все контакты с такой фамилией и их номера телефонов. Поиск не должен зависеть
# от регистра символов.
# Пример работы программы:
# Введите номер действия:
# 1.	Добавить контакт.
# 2.	Найти человека.
# При выборе действия 1:
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
# Введите номер телефона: 888
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
# Введите номер действия:
# 1.	Добавить контакт
# 2.	Найти человека
# При выборе действия 1:
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
# Такой человек уже есть в контактах.
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
# Введите номер действия:
# 1.	Добавить контакт
# 2.	Найти человека
# При выборе действия 1:
# Введите имя и фамилию нового контакта (через пробел): Алиса Петрова
# Введите номер телефона: 999
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}
# Введите номер действия:
# 1.	Добавить контакт
# 2.	Найти человека
# При выборе действия 2:
# Введите фамилию для поиска: Сидоров
# Иван Сидоров 888
# Введите номер действия:
# 1.	Добавить контакт
# 2.	Найти человека

def add_contact(dict_phonebook):
    name = input('Name: \n'
                 '>: ')
    tuple_name = tuple(name.split(' '))
    if tuple_name in dict_phonebook:
        print('Such a person is already in phonebook:\n'
              f'{tuple_name}: {dict_phonebook[tuple_name]}')
    else:
        number = int(input('Phone number:\n'
                           '>: '))
        dict_phonebook[tuple_name] = number
    return dict_phonebook


def search_contact(dict_phonebook):
    name = input('Name: \n'
                 '>: ')
    found = False
    for key_name, value_number in dict_phonebook.items():
        if name in key_name[0]:
            print(f'{key_name}: {value_number}')
            found = True
        elif name in key_name[1]:
            print(f'{key_name}: {value_number}')
            found = True
    if not found:
        print('Such a person has not been found.')
    return dict_phonebook


def show_contacts(dict_phonebook):
    for key_name, value_number in sorted(dict_phonebook.items()):
        print(f'{key_name}: {value_number}')


def main_menu(dict_phonebook):
    action = input('\nEnter the action number:\n'
                   '\t1. Add a contact\n'
                   '\t2. Find a person\n'
                   '\t3. Show all phonebook\n'
                   '>: ')
    if action == '1':
        add_contact(dict_phonebook)
    elif action == '2':
        search_contact(dict_phonebook)
    elif action == '3':
        show_contacts(dict_phonebook)
    else:
        print('Wrong action.')
    return True


dict_phonebook = {}
while True:
    main_menu(dict_phonebook)
