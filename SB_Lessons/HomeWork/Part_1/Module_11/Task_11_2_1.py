# Задача 1. Ставки на спорт
# Нас наняла букмекерская контора, где проводятся ставки на конный спорт. Напишите программу расчёта потенциального
# выигрыша игрока. Для этого вводится его ставка в рублях и коэффициент (вещественное число), а выводится
# их произведение в качестве потенциального выигрыша.
# Пример:
# Сколько ставим? 1234
# Какой коэффициент? 1.716
# Потенциальный выигрыш: 2117.544

bet = int(input('Your bet: '))
k = float(input('Enter ratio: '))

win = bet * k
win = round(win, 2)

print('Potential gain: {sum}'.format(sum=win))
# print('Potential gain: {sum:,d}'.format(sum=(win)).replace(',', ' '))
