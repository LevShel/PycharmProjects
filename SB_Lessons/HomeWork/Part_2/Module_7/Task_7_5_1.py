# Задача 1. Паспортные данные
# В базе данных поликлиники хранятся паспортные данные людей. Хранение реализовано
# с помощью словаря, состоящего из пар «Серия и номер паспорта — фамилия и имя».
# Серия и номер — составной ключ, а фамилия и имя — составное значение.
#
data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}
#
# Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека.

passport_seria = int(input('Enter passport seria: '))
passport_number = int(input('Enter passport number: '))
tuple_passport = (passport_seria, passport_number)
if tuple_passport in data:
    surname, name = data[tuple_passport]
    print(f'>>> {name} {surname}')
else:
    print('No data found for the provided passport.')
