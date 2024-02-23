# Задача 2. Почта 2
# На почте немного поменялись правила: теперь в почтовом извещении нужно указывать
# фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.
# Реализуйте функцию, которая получает все эти данные и выводит на экран.
# В программе вызовите функцию три раза с разными значениями аргументов.
#
# Подсказка: семь аргументов.

def input_info():
    s_name = input('Surname: ')
    f_name = input('Name: ')
    country = input('Country: ')
    city = input('City: ')
    street = input('Street: ')
    building = input('Building: ')
    flat = input('Flat: ')
    print()
    return s_name, f_name, country, city, street, building, flat


def info():
    s_name, f_name, country, city, street, building, flat = input_info()
    print(f'Фамилия: \t{s_name}')
    print(f'Имя: \t\t{f_name}')
    print(f'Страна: \t{country}')
    print(f'Город: \t\t{city}')
    print(f'Улица: \t\t{street}')
    print(f'Дом: \t\t{building}')
    print(f'Квартира: \t{flat}')
    print()


info()
info()
info()