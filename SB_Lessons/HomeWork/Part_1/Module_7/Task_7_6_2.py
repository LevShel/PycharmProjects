# Задача 2. Посчитай чужую зарплату...
# Что нужно сделать
# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании и,
# чтобы облегчить себе жизнь, обратилась к программисту.
# Напишите программу, которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

total_salary = 0
middle_salary = 0

i = 0
for month in range(12):
    i += 1
    salary = float(input(f'{i} month salary: '))
    total_salary += salary
middle_salary = total_salary / i
print(f'middle_salary = {round(middle_salary, 2)}')