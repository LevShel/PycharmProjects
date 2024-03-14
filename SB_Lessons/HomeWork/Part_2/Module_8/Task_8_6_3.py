# Задача 3. Помощь другу
# Нашего друга попросили написать функцию, которая на вход принимает список
# всякого мусора. Ему нужно подготовить из этого списка список словарей, чтобы
# его коллеги смогли дальше продолжить обработку данных. Вот список правил,
# что нужно сделать с изначальным списком:
# Если в списке встретился словарь, то оставляем его.
# Если в списке встретилась строка, то из неё нужно сделать словарь и положить
# его в итоговый список, например  “abc” → {“abc”: “abc”}.
# С числами нужно сделать то же самое, что и со строками.
# Всё остальное выкидываем из нашего списка.
#
# Друг написал программу, но в ней ошибка, так как она что-то не то выводит :(
# Нужна ваша помощь, вот сама программа:
# def create_dict(data, template=dict()):
#     if isinstance(data, dict):
#         return data
#     if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
#         return template[data] = data
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         new_list.append(create_dict(i_element))
#     return new_list
#
# data = [“sad”, {“sds”: 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)
#
# Исправьте программу и убедитесь, что всё работает верно.

def create_dict(data, template=None):
    if isinstance(data, dict):
        return data
    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        if template is None:
            template = {}
        return {data: data}


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element))
    return new_list


data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)
