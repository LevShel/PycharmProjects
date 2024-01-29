# Задача 6. Вклады
# Что нужно сделать
# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается. Определите,
# через сколько лет вклад составит не менее Y рублей.
# Напишите программу, которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

year = 0
x = float(input('The deposit in the bank is, rubles: '))
p = float(input('It increases annually by, %: '))
y = float(input('The contribution will be at least rubles: '))

while x < y:
    year += 1
    x += x * (p / 100)
    x = int(x)

print(f'\nYou need {year} years.')
