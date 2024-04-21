from typing import List

my_mums: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
other_nums: List[int] = [2, 7, 1, 8, 2, 8, 1, 8]
# список из сумм элементов двух списков:
result: List[int] = list(map(lambda x, y: x + y, my_mums, other_nums))
print(result)


