# Задача 3. Повышение цен
# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт
# о себе знать, мы спрогнозировали, что через год придётся повышать цены на X процентов,
# а ещё через один год — ещё на Y процентов.
# Напишите программу, которая получает на вход список цен на товары
# (вещественные числа, список генерируется также с помощью list comprehensions)
# и выводит в одну строку общую сумму стоимости товаров за каждый год.
#
# Пример:
# Цена на товар: 1.09
# Цена на товар: 23.56
# Цена на товар: 57.84
# Цена на товар: 4.56
# Цена на товар: 6.78
# Повышение на первый год: 0
# Повышение на второй год: 10
#
# 93.83 93.83 103.21

prices = [float(input('Good`s price: ')) for price in range(5)]

first_up = int(input('1st price up: '))
second_up = int(input('2nd price up: '))

first_year = [price+first_up for price in prices]
second_year = [price+second_up for price in first_year]

print(f'Promotion for the 1st year: {first_up}\n'
      f'Promotion for the 2nd year: {second_up}\n'
      f'The sum of prices for each year: {sum(prices)}, {sum(first_year)}, {sum(second_year)}')