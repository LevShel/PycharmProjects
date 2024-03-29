# Задача 2. Коллекторы
# Что нужно сделать
# Напишите робота для коллекторов. В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, пока должник не введёт нужную сумму
# (равную сумме долга или больше). После погашения долга робот сообщает об этом пользователю
# и благодарит его.
# Пример
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
# Рекомендация
# Обратите внимание: считать сумму внесённых средств не нужно, это не соответствует условию задачи.

name = input('Your name: ')
debt = float(input('The amount of debt: '))
print(f'\n{name}, your debt is {debt} rub.')

while debt != 0:
    cash_in = float(input('How many rubles will you deposit right now to pay it off? '))
    debt -= cash_in
    if debt > 0:
        print(f'It`s not enough, {name}. Let`s do it again.')
print(f'Great, {name}! You have paid off the debt. Thanks!')