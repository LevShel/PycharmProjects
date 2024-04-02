# Сервер генерирует числа от 1 до 100.
# Создать копию этого списка с числами, которые делятся на 10.
# Третий элемент списка обнулить.
# Вывести элементы 2...7 этого списка.

nums = [x for x in range(1, 101) if x % 10 == 0]
new_nums = nums[:]
new_nums[3] = 0

print(nums)

# for i in range(2, 8):
#     print(new_nums[i], end=' ')

print(new_nums[2:8], end=' ')