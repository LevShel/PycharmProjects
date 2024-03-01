# Задача 2. Магазин
# У нас есть вот такой список цен на некоторые товары из магазина:
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# В этом списке также хранятся цены на товары, которые уже давно не продаются.
# По какой-то причине система, вместо того чтобы их занулить, просто приписала
# к ним минус. Нам нужно это исправить.
# Напишите программу, которая генерирует новый список из первого списка, заменяя
# все отрицательные числа на ноль.
#
# Результат:
# [1.25, 0, 10.22, 3.78, 0, 1.16]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

actual_prices = [price if price > 0 else 0 for price in original_prices]
print(actual_prices)
