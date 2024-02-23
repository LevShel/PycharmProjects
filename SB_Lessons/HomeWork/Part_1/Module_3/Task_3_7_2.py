# Задача 2. Финансовый отчёт
# Что нужно сделать
# Васе пришло очередное задание — автоматизация финансовой отчётности.
# Звучит сложно, а на деле нужно просто написать код,
# который будет считать нужные для отчёта вычисления автоматически.
# Вычисления, которые нужно реализовать в программе:
# сумму дохода первых двух кварталов поделить на сумму послед-них двух кварталов,
# чтобы понять динамику роста или падения дохода.
# Алгоритм действий в программе:
# 1.	Запросить у пользователя четыре числа.
# 2.	Отдельно сложить два первых и два вторых.
# 3.	Разделить первую сумму на вторую.
# 4.	Вывести результат на экран.

first_quarter = float(input('Enter sum of 1st quarter: '))
second_quarter = float(input('Enter sum of 2nd quarter: '))
third_quarter = float(input('Enter sum of 3rd quarter: '))
fourth_quarter = float(input('Enter sum of 4th quarter: '))

first_half = first_quarter + second_quarter
second_half = third_quarter + fourth_quarter
res = first_half / second_half

print('\nResult is: ', round(res, 2))