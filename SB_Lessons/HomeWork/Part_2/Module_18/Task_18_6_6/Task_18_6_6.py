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


def unpack_dict(d):
    for key, value in d.items():
        if not isinstance(value, dict) and not isinstance(value, list):
            print(f'{key}: {value}')
            input()
        elif isinstance(value, list):
            for item in value:
                print(key)
                unpack_dict(item)
        else:
            print(key)
            unpack_dict(value)


with open('json_old.json', 'r', encoding='utf-8') as file:
    data_old = json.load(file)
with open('json_new.json', 'r', encoding='utf-8') as file:
    data_new = json.load(file)

# TODO
unpack_dict(data_old)
# for key, value in data_old.items():
# if not isinstance(value, dict):
#     print(f'{key}: {value}')
#     input()
# if data_old[key] != data_new[key]:
# with open('result.json', 'w') as file:
#     json.dump(f'{key}: {value}', file, indent=4)
# TODO
