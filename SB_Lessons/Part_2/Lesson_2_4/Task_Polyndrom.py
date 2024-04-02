# Исходные данные:
nums = []
mirror_nums = []
palindrome_nums = []
num = ''

# Ввод массива
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

# Зеркальный массив
jj = 0
while jj != len(nums):
    mirror_nums.append(nums[len(nums)-jj-1])
    jj += 1

# Создание полиндрома
palindrome_nums.extend(nums)
j = 2
while j != len(nums)+1:
    while nums[len(nums)-j] == nums[len(nums)-j+1]:
        j += 1
    added = nums[len(nums)-j]
    palindrome_nums.append(added)
    j += 1

# Вывод введённого массива
print('\nEntering nums:')
for _ in nums:
    print(_, end=' ')

# Зеркальный массив
print('\nMirror nums:')
for _ in mirror_nums:
    print(_, end=' ')

# Вывод полиндрома
print('\nPalindrome:')
for _ in palindrome_nums:
    print(_, end=' ')