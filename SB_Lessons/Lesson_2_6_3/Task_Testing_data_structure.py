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

# До этого что-то происходит
print(data.get('server'))

data['server'] = {
    'host': '127.0.0.1',
    'port': '10'
}

# До этого что-то происходит
if data.get('configuration', {}).get('ssh', {}).get('login', {}):
    print('There is login in structure')
print(data.get('configuration', {}).get('ssh', {}).get('login', {}))

data['configuration'] = {
    'ssh': {
        'access': 'true',
        'login': 'Ivan',
        'password': 'qwerty'
    }
}

print(data)