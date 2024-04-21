from typing import List

result: List[int] = [4, 8, 15, 16, 23, 42]
# сумма чётных чисел списка:
result_sum_even: int = sum(map(lambda num: num, filter(lambda x: x % 2 == 0, result)))
print(result_sum_even)
