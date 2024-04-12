def fibonacci(number):
    current_value = 0
    next_value = 1
    for _ in range(number):
        yield current_value
        current_value, next_value = next_value, current_value + next_value


fib_seq = fibonacci(number=10)
for i_value in fib_seq:
    print(i_value)