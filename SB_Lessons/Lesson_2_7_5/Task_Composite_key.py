# Исходный словарь с сотавным ключом из фамилии и имени
phonebook_dict = {
    ('Petrov', 'Vanya'): 89991234567,
    ('Sidorov', 'Petya'): 89992345678,
    ('Ivanov', 'Ilya'): 89993456789,
}

# Добавление новой записи в словарь
phonebook_dict[('Ivanov', 'Dima')] = 89994567890

print(phonebook_dict)

# Поиск в словаре по фамилии Иванов (часть составного ключа)
for i_person in phonebook_dict:
    if 'Ivanov' in i_person:
        print(i_person[1], phonebook_dict[i_person])