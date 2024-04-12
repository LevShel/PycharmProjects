def fibonacci(number):
    current_value = 0
    next_value = 1
    for _ in range(number):
        yield current_value
        current_value, next_value = next_value, current_value + next_value
        if current_value > 10 ** 6:  # ограничиваем поседовательность до 1 000 000
            return


def square(nums):
    for num in nums:
        yield num ** 2


fib_seq = fibonacci(number=999999999999)
for i_value in fib_seq:
    print(i_value, end=' ')
print('\n')

# генератор от генератора:
print(sum(square(fibonacci(number=5000))))  # сумма квадратов числел от 0 до 5 000
print('\n')

# генераторные выражения:
cubes_gen = (num ** 3 for num in range(10))  # генерируем список кубов чисел от 0 до 10, не создавая генератор
for i_num in cubes_gen:
    print(i_num, end=' ')
