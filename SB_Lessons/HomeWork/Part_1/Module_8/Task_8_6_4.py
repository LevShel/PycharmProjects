# Задача 4. Среднее на отрезке
# Что нужно сделать
# Напишите программу, которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b],
# кратных числу c.
# Рекомендации
# Функция range(start, stop) не включает границу stop, останавливается, не доходя до неё.

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print(f'\nSection [{a}; {b}]\n')

sum_nums = []

for num in range(a, b+1):
    if num % c == 0:
        sum_nums.append(num)

average = sum(sum_nums) / len(sum_nums)
print(f'The arithmetic mean of all the numbers from the segment [{a}; {b}],\n'
      f'multiples of the number {c} is {average}')