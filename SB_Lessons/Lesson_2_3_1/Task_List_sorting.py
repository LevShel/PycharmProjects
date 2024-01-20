# Входные данные:
# nums - список из N чисел.
# Выходные данные:
# Отсортированный по возрастанию значений список nums.

nums = []
num = int
sorting_list = []

print('Enter nums. For stop enter "0"')
while num != 0:
    num = int(input('>: '))
    nums.append(num)

sorting_list = sorted(nums)

print('\nEntering list:', end=' ')
for i in range(0, len(nums)-1):
    print(nums[i], end=' ')

print('\nSorting list:', end=' ')
for i in range(1, len(sorting_list)):
    print(sorting_list[i], end=' ')