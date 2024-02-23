# Задача 5. Отрезок
# Что нужно сделать
# Напишите программу, которая считывает с клавиатуры два числа: a и b,
# — считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b],
# кратных числу 3.

first_num = int(input('Enter 1st num: '))
second_num = int(input('Enter 1st num: '))

div_3 = []
sum_div_3 = 0
average = 0

for num in range(first_num, second_num+1):
    if num % 3 == 0:
        div_3.append(num)

for num in div_3:
    sum_div_3 += num
average = sum_div_3 / len(div_3)
# average = round(average, 2)

print(f'\nThe arithmetic mean of all the numbers \n'
      f'from the segment [{first_num}; {second_num}], \n'
      f'multiples of the number 3 is: {average}')