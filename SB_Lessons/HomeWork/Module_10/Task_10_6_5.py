# Задание 5. Наибольшая сумма цифр
# Что нужно сделать
# Пользователь вводит N чисел. Среди натуральных чисел, которые он указал, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.

# nums = int(input('Enter num of nums: '))
#
# local_sum = 0
# max_num = 0
# local_num = 0
#
# for i in range(nums):
#     num = int(input('Enter num: '))
#     if max_num < num < 10:
#         max_num = num
#     if local_sum < num > 9:
#         while num != 0:
#             local_num = num % 10
#             local_sum += local_num
#             num = num // 10
#             max_num = local_sum
# print(max_num)


n = int(input('Enter num of nums: '))

max_number = 0
max_sum_of_digits = 0

for _ in range(n):
    number = int(input('Enter num: '))

    sum_of_digits = 0
    current_number = number
    while current_number > 0:
        sum_of_digits += current_number % 10
        current_number //= 10

    if sum_of_digits > max_sum_of_digits:
        max_sum_of_digits = sum_of_digits
        max_number = number

print(f'Max num by sum of nums: {max_number}')
print(f'Sum of nums in num: {max_sum_of_digits}')
