# Задача 1. Космическая еда
# Что нужно сделать
# Ваш космический корабль потерпел крушение на пустынной планете.
# Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки.
# Из прошлого опыта вы знаете, что если будете экономно питаться,
# то у вас будет уходить по четыре килограмма гречки в месяц.
# Чтобы прикинуть гречневый бюджет, вы решили написать программу,
# которая выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе
# через месяц, два и так далее, пока она не закончится. Используйте цикл for.

month = 0

for kilos in range(100, 0, -4):
    month += 1
    print(f'Month {month}: there are {kilos} of buckhweat.')