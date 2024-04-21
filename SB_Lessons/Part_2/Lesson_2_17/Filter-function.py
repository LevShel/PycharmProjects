from typing import List

result: List[int] = [4, 8, 15, 16, 23, 42]
# вывод только чётных элементов списка:
result_even: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(result_even)
