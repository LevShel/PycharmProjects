def is_palindrome(nums):
    mirror_nums = nums[::-1]
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

answer = []
for i_nums in range (0, len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break


palindrome_nums = []
palindrome_nums = nums + answer

            # Вывод введённого массива
print('\nEntering nums:', nums[:])

            # Зеркальный массив
print('\nReverse nums:', nums[::-1])

            # Вывод пaлиндрома
print('\nPalindrome:', palindrome_nums)