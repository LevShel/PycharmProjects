# Задание 2. Криптовалюта
# Что нужно сделать
# При работе с API (application programming interface) сайта биржи по криптовалюте
# вы получили такие данные в виде словаря: см. API.py.
# Теперь необходимо обработать эти данные.
# Напишите программу, которая выполняет следующий алгоритм действий:
# 1.	Вывести списки ключей и значений словаря.
# 2.	В ETH добавить ключ total_diff со значением 100.
# 3.	Внутри fst_token_info значение ключа name поменять с fdf на doge.
# 4.	Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений
# в total_out внутри ETH.
# 5.	Внутри sec_token_info изменить название ключа price на total_price.
# После выполнения алгоритма выводить результат (словарь) не нужно.
# Советы и рекомендации
# •	Если вы достали из словаря список по ключу, то можете применять к нему методы списка.
# Например:
# словарь[“список”].append(123)
# Python возьмёт из словаря объект по ключу «список» и применит к нему метод append.
# Эта же логика работает с другими типами данных. Например, если вы достали из словаря
# словарь, то к нему можно применять методы словаря, а если достали строку — методы строк.
# •	Чтобы не запутаться, распечатывайте объект, который получаете в данный момент.
# Также можно распечатать тип объекта:
# print(data)
# print(data[‘ключ’], type(data[‘ключ’]))
# print(data[‘ключ’][0], type(data[‘ключ’][0]))
# и так далее.
# Так вы всегда будете понимать, над каким объектом работаете в данный момент.

import API

# 1. Вывести списки ключей и значений словаря.
print("Keys:", list(API.data.keys()))
print("Values:", list(API.data.values()))

# 2. В ETH добавить ключ total_diff со значением 100.
API.data["ETH"]["total_diff"] = 100

# 3. Внутри fst_token_info значение ключа name поменять с fdf на doge.
API.data["tokens"][0]["fst_token_info"]["name"] = "doge"

# 4. Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
total_out_sum = sum(token.pop("total_out") for token in API.data["tokens"])
API.data["ETH"]["totalOut"] += total_out_sum

# 5. Внутри sec_token_info изменить название ключа price на total_price.
for token in API.data["tokens"]:
    if "sec_token_info" in token:
        sec_token_info = token["sec_token_info"]
        sec_token_info["total_price"] = sec_token_info.pop("price")

# Результат
print("Modified data:", API.data)