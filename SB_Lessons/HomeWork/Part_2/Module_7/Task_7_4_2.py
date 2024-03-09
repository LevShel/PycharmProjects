# Задача 2. Сервер
# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:
server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
#
# Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно,
# как они представлены в словаре.
# Результат работы программы:
# server:
#     host: 127.0.0.1
#     port: 10
# configuration:
#     access: true
#     login: Ivan
#     password: qwerty

for key1, value1 in server_data.items():
    if isinstance(value1, dict):
        print(f'{key1}:')
        for key2, value2 in value1.items():
            print(f'\t{key2}: {value2}')
    else:
        print(f'{key1}: {value1}')
        