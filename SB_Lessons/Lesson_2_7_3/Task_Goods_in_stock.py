# Исходные данные "со склада"
goods = {
    'Lamp': '12345',
    'Table': '23456',
    'Sofa': '34567',
    'Chair': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Результат работы программы:
# Lamp - 27 pcs., total price: 1134 rub.
# Table - 54 pcs., total price: 27860 rub.
# Sofa - 3 pcs., total price: 3550 rub.
# Chair - 105 pcs., total price: 10311 rub.

print('goods', goods)
print('store', store)
print()

# for i_title, i_code in goods.items():
#     for j_code, j_info in store.items():
#         if i_code == j_code:
#             print(i_title, j_info)

for i_title, i_code in goods.items():
    total_quantity = 0
    total_price = 0
    for i_good in store[i_code]:
        total_quantity += i_good['quantity']
        total_price += i_good['price'] * i_good['quantity']
    # print(i_title,' - ', total_quantity,'pcs., total price: {:,d}'.format(total_price).replace(',',' '), 'rub.')
    print('{title} - {quantity:,d} pcs., total price: {price:,d} rub.'.format(
        title=i_title,
        quantity=total_quantity,
        price=total_price
    ).replace(',', ' '))
# print('There are {:,d} details in stock.'.format(quantity).replace(',', ' '))