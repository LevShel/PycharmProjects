# Задача 2. Поиск элемента — 2
# Что нужно сделать
# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную
# глубину — уровень, до которого будет просматриваться структура.
# Напишите функцию, которая находит заданный пользователем ключ в словаре
# и выдаёт значение этого ключа на экран. По умолчанию уровень не задан.
# В качестве примера можно использовать такой словарь:
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


# Пример 1
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}
# Пример 2
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None

def find_key(struct, key, max_depth, current_depth=0):
    if key in struct:
        return struct[key]
    if max_depth is not None and current_depth >= max_depth:
        return None
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_depth, current_depth + 1)
            if result:
                return result
    return None


user_key = input('Введите искомый ключ: ')
max_depth_input = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if max_depth_input == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
else:
    max_depth = None

value = find_key(site, user_key, max_depth)
if value is not None:
    print(f'Значение ключа: {value}')
else:
    print('Заданный ключ не найден или превышена максимальная глубина.')
