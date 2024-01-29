# Задача 6. Новоселье
# Что нужно сделать
# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении, какую купить квартиру, исходя из предпочтений и семейного бюджета,
# они остановились на двух вариантах:
# 1.	Выбрать квартиру попросторнее (не менее 100 м2), но стоимостью не более 10 млн.
# 2.	Немного расширить круг поиска, то есть выбрать квартиру поменьше (от 80 м2),
# но и стоимостью не более 7 млн.
# Напишите программу, которая получает на вход стоимость квартиры и её площадь
# и выводит сообщение, подходит ли она.

price = float(input('Enter price (in millions): '))
square = float(input('Enter square (in m^2): '))


if square >= 100 and price <= 10:
    print('Perfect variant!')
elif square >= 80 and price <= 7:
    print('Nice variant!')
else:
    print('Don`t match.')