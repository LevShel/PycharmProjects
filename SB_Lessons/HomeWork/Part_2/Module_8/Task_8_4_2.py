# Задача 2. Непонятно!
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами,
# ссылками, объектами и их id. Видя, как он мучается, вы решили помочь ему
# и объяснить эту тему наглядно.
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип
# введённых данных, информацию о его изменяемости, а также id этого объекта.
# Помните, что через input можно получить только строку, что бы вы ни вводили.
# В данном случае ввод можно выполнить вручную, просто вписав нужный объект
# в переменную, без использования функции input.
#
# Пример 1:
# Введите данные: привет
#
# Тип данных: str (строка)
# Неизменяемый (immutable)
# Id объекта: 1705156583984
#
# Пример 2:
# Введите данные: {‘a’: 10, ‘b’: 20}
#
# Тип данных: dict (словарь)
# Изменяемый (mutable)
# Id объекта: 1705205308536

def is_string(obj):
    if obj.startswith('{') and obj.endswith('}'):
        return dict
    if obj.startswith('(') and obj.endswith(')'):
        return tuple
    if obj.startswith('[') and obj.endswith(']'):
        return list
    if obj.startswith("'") and obj.endswith("'"):
        return str
    if obj.isdigit():
        return int


def is_immutable(obj):
    immutable_types = (int, float, complex, str, tuple, frozenset)
    mutable_types = (list, dict, set)
    if is_string(string_input) in immutable_types:
        return 'Immutable'
    if is_string(string_input) in mutable_types:
        return 'Mutable'


string_input = input('>: ')

print(f'Type: {is_string(string_input)}\n'
      f'{is_immutable(string_input)}\n'
      f'ID: {id(string_input)}')