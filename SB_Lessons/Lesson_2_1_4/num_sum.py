number = int(input('Any number: ')) # 1234

num_sum = 0
original_number = number

while number !=0:
    last_num = number % 10  # 4...3...2...1
    num_sum += last_num # 0+4...4+3...7+2...9+1 = 10
    number //= 10

print('Sum of nums ',original_number, ' = ', num_sum)