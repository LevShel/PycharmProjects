# {
#     'server': {
#         'host': '127.0.0.1',
#         'port': '10'
#     },
#     'configuration': {
#         'ssh': {
#             'access': 'true',
#             'login': 'Ivan',
#             'password': 'qwerty'
#         }
#     }
# }

data = dict()
data['server'] = {
    'host': '127.0.0.1',
    'port': '10'
}
data['configuration'] = {
    'ssh': {
        'access': 'true',
        'login': 'Ivan',
        'password': 'qwerty'
    }
}

print()
print(data) # Вывод всего словаря
print()
print(data['server']) # Вывод данных из словаря "server"
print()
print(data['server']['port']) # Вывод значения "port"
print()
print(data['configuration']['ssh']) # Вывод данных вложенного словаря "ssh"
print()
data['configuration']['ssh']['login'] = 'Vova' # Изменение значения для ключа "login"

for i_value in data.values(): # Красивый вывод словарей
    for i_key in i_value:
        print(i_key, i_value[i_key])