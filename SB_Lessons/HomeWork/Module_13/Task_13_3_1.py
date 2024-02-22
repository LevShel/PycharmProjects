# Задача 1. Возможности компьютера
# В одной IT-компании тестируют возможности различных языков программирования,
# компиляторов и, конечно же, компьютеров. Компания дала вам задачу понять,
# какое самое маленькое возможное число можно получить путём постоянного деления числа на 2.
# Изначально число равно единице. Также, помимо самого числа, компания просит
# вывести количество делений. Реализуйте такую программу.

def divider_cycle(n):
    i = 0
    while n > 0:
        i += 1
        n /= 2
        if n != 0:
            min_num = n
        else:
            break
    print(f'The smallest possible number: {min_num}\n'
          f'Number of divisions: {i-1}')


num = int(input('Enter num: '))
divider_cycle(num)
