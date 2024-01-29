# Задача 4. Калькулятор скидки
# Что нужно сделать
# Васин друг переехал в новую квартиру, и ему нужно купить три стула в разные комнаты.
# Цены на стулья разные, а в некоторых магазинах есть скидки.
# Друг хочет заказать у Васи калькулятор скидки, чтобы проще ориентироваться в ценах.
# Напишите программу, которая запрашивает три стоимости товара и вычисляет сумму чека.
# Если сумма чека превышает 10 000 руб., нужно вычесть из этой суммы скидку 10%
# (умножить на 10, разделить на 100). Итого-вая сумма должна выводиться на экран.

chair_1 = float(input('Enter 1st chair price: '))
chair_2 = float(input('Enter 2nd chair price: '))
chair_3 = float(input('Enter 3rd chair price: '))

sum = chair_1 + chair_2 + chair_3
discount = sum * 0.1
disc_sum = sum - discount

if sum > 10000:
    print('Sum is more than 10k. You have discount!\n'
          f'Final price is: {round(sum, 2):,.2f}'.replace(',', ' '))
else:
    print(f'Total price is: {round(disc_sum, 2):,.2f}'.replace(',', ' '))