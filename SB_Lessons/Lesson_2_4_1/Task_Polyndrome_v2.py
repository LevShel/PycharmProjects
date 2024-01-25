def is_palindrome(nums):
    mirror_nums = []
    for i_num in range(len(nums)-1, -1, -1):
        mirror_nums.append(nums[i_num])
    if nums == mirror_nums:
        return True
    else:
        return False

# Ввод массива
nums = []
i = 1
while True:
    print('Enter the ', i, ' num (or enter "end" to complete):')
    num = input('> ')
    i += 1
    if num.lower() == 'end':
        i -= 1
        print('\nOk!\n')
        break
    nums.append(num)

new_nums = []
answer = []
for i_nums in range (0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

palindrome_nums = []
palindrome_nums = nums + answer

# Вывод введённого массива
print('\nEntering nums:')
for _ in nums:
    print(_, end=' ')

# Зеркальный массив
print('\nCenter of palindrome:')
for _ in new_nums:
    print(_, end=' ')

# Вывод пaлиндрома
print('\nPalindrome:')
for _ in palindrome_nums:
    print(_, end=' ')