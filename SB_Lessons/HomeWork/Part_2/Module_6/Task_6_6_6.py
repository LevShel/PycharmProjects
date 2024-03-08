# Задание 6. Пицца
# Что нужно сделать
# В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и сколько
# заказывал у них в определённый период. Вам нужно структурировать эту информацию
# и определить, сколько всего пицц купил каждый заказчик.
# На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида
# «Покупатель — название пиццы — количество заказанных пицц». Реализуйте код, который
# выводит список покупателей и их заказов по алфавиту. Учитывайте, что один человек может
# заказать одну и ту же пиццу несколько раз.
# Пример
# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5
# Иванов:
# Мексиканская: 2
# Мясная: 3
# Пепперони: 3
# Петров:
# Де-Люкс: 2
# Интересная: 5

dict_orders = {}
orders = int(input('Enter num of orders: '))
for i in range(1, orders + 1):
    str_order = input(f'{i} order: ')
    customer, pizza_name, pizza_num = str_order.split(' ')
    if customer not in dict_orders:
        dict_orders[customer] = {pizza_name: int(pizza_num)}
    elif pizza_name in dict_orders[customer]:
        dict_orders[customer][pizza_name] += int(pizza_num)
    else:
        dict_orders[customer][pizza_name] = int(pizza_num)
for customer, pizza in sorted(dict_orders.items()):
    print(f'{customer}:')
    for pizza_name, pizza_num in sorted(pizza.items()):
        print(f'{pizza_name}: {pizza_num}')
