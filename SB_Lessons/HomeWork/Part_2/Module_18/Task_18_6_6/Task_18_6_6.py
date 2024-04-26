# Задача 6. Поиск разницы между двумя JSON-файлами (пример из реального тестового задания
# на должность Python-разработчика уровня Junior)
# Что нужно сделать
# Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list, выведите различие.
# Иными словами, вам нужно отловить изменение определённых параметров и вывести значение: что изменилось и на что.
# Набор ключей в обоих файлах идентичный, различаются лишь значения.
# Напишите программу, которая:
# загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
# выполняет сравнение параметров, указанных в diff_list;
# формирует результат в виде словаря;
# записывает словарь в JSON-файл с названием result.json.
# Исходные данные
# Файлы:
# json_old.json,
# json_new.json.
# Список параметров для отслеживания (можно сформировать инпутом или ввести вручную):
# diff_list = [‘services’, ‘staff’, ‘datetime’]
# Формат итогового словаря с результатом:
# Словарь {параметр: новое_значение, ….}
# Пример
# Данные, загруженные из json_old.json:
# {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111,
#           'company_id': 111111, 'services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500,
#           'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
#           'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2,
#           'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00',
#           'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1,
#           'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049,
#           'created_user_id': 10573443, 'deleted': False, 'paid_full': 0,
#           'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
# Данные, загруженные из json_new.json:
# {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111,
#       'company_id': 111111, 'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500,
#       'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
#       'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2,
#       'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T13:00:00+03:00',
#       'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 2, 'confirmed': 1,
#       'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049,
#       'created_user_id': 10573443, 'deleted': False, 'paid_full': 1,
#       'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
# diff_list = [‘services’, ‘staff’, ‘datetime’]
# Результат
# print(result)
# В консоли должно вывестись следующее сообщение:
# {'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500,
#       'first_cost': 1500, 'amount': 1}], 'datetime': '2022-01-25T13:00:00+03:00'}
# Помимо вывода в консоль, должен быть сформирован JSON-файл с получившимся словарём (result.json).
# Обратите внимание: в result представлены не все изменившиеся поля, а лишь те, что объявлены в diff_list.

import json
from typing import Any


def unpack_dict(_dictionary: Any) -> None:
    """
    Функция распаковки словаря из json-файла.
    """
    for _key, _value in _dictionary.items():
        if (not isinstance(_value, dict) and
                not isinstance(_value, list)):
            print(f'{_key}: {_value}')
        elif isinstance(_value, list):
            if not _value:
                print(f'{_key}: ')
            else:
                for _item in _value:
                    print(f'{_key}:')
                    unpack_dict(_item)
        else:
            print(f'{_key}:')
            unpack_dict(_value)


def unpack_list(_list: list) -> Any:
    """
    Функция для распаковки списка.
    """
    for _item in _list:
        # print(_item)
        return _item


def read_json(filename: str) -> Any:
    """
    Функция для чтения данных из json-файла.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def write_json(filename: str, data: Any) -> None:
    """
    Функция для записи данных в json-файл.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json_data = json.dumps(data, indent=4)
        file.write(json_data)


data_old = read_json(filename='json_old.json')
data_new = read_json(filename='json_new.json')

diff_list = []
for key, value in data_old.items():
    if data_old[key] != data_new[key]:
        # print(f'{key}: {value}')
        diff_list.append({key: value})

write_json(filename='result.json', data=unpack_list(_list=diff_list))

result = read_json(filename='result.json')
unpack_dict(result)
