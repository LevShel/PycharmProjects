# Задача 2. Функция максимума
# Что нужно сделать
# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало
# проще работать. Он захотел написать функцию, которая будет находить максимум
# из перечисленных чисел. Функция для нахождения максимума из двух чисел у него уже есть.
# Юра задумался: может быть, её можно как-то использовать для нахождения максимума
# уже от трёх чисел?
# Помогите Юре написать программу, которая находит максимум из трёх чисел. Для этого
# используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:
# 1.	maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2.	maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх);
# при этом она должна использовать для сравнений первую функцию maximum_of_two.

def two_nums():
    a = int(input('Enter 1st num: '))
    b = int(input('Enter 2nd num: '))
    return a, b


def three_nums():
    c = int(input('Enter 3rd num: '))
    return c


def maximum_of_two():
    a, b = two_nums()
    max_of_2 = max(a, b)
    return max_of_2


def maximum_of_three():
    c = three_nums()
    max_of_2 = maximum_of_two()
    max_of_3 = max(max_of_2, c)
    return max_of_3


nums = int(input('Enter num of nums: '))
if nums == 2:
    max_num = maximum_of_two()
    print(f'Max is: ', max_num)
elif nums == 3:
    max_num = maximum_of_three()
    print(f'Max is: ', max_num)
else:
    print('Enter 2 or 3 nums.')