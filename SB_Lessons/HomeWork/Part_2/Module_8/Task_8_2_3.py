# Задача 3. Поиск элемента
# Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо
# пройтись по ней и найти нужный элемент. Для этого в программировании используются
# специальные алгоритмы поиска.
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт
# значение этого ключа на экран. В качестве примера можно использовать такой словарь:
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# Пример 1:
# Искомый ключ: h2
# Значение: Здесь будет мой заголовок
# Пример 2:
# Искомый ключ: abc
# Такого ключа в структуре сайта нет.

def find_key(struct, key):
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'My site'
        },
        'body': {
            'h2': 'Here is heading',
            'div': 'Here is any block',
            'p': 'Here is new paragraph'
        }
    }
}

user_key = input('Key: ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print(f'There is no key "{user_key}"')
