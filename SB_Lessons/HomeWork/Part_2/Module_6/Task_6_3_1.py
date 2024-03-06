# Задача 1. Заказ фруктов
# В торговую компанию пришёл заказ:
# order = {'apple': 2,
#          'banana': 3,
#          'pear': 1,
#          'watermelon': 10,
#          'chocolate': 5}
# Ключи — названия товаров, значения — необходимое количество килограммов.
# При помощи метода get и установки значения по умолчанию проверьте, есть ли товар на складе,
# и получите его цену. Если товара нет, то по умолчанию получите 0. Подсчитайте итоговую
# выручку компании по имеющимся товарам.
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
# Ключи — названия товаров, значения — цена за один килограмм.
# Напишите программу, которая суммирует стоимость (цена × количество) всех заказанных
# товаров, и выведите итоговую сумму в консоль.

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}
print('Available to order:')
bill = 0
for key, value in order.items():
    if key in incomes:
        bill += (incomes[key] * order[key])
        print(f'{key}: {value} * {incomes[key]} = {value * incomes[key]}')
print(f'TOTAL: {bill}')
