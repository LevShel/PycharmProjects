# Задача 3. Анализ данных
# Отдел анализа данных сегодня получил вот такую интересную штуку:
# 0   -1  -2  -3  -4  -5  -6  -7  -8  -9
# 1   0   -1  -2  -3  -4  -5  -6  -7  -8
# 2   1   0   -1  -2  -3  -4  -5  -6  -7
# 3   2   1   0   -1  -2  -3  -4  -5  -6
# 4   3   2   1   0   -1  -2  -3  -4  -5
# 5   4   3   2   1   0   -1  -2  -3  -4
# 6   5   4   3   2   1   0   -1  -2  -3
# 7   6   5   4   3   2   1   0   -1  -2
# 8   7   6   5   4   3   2   1   0   -1
# 9   8   7   6   5   4   3   2   1   0
# Вам, как работнику этого отдела, дали задание понять, как и почему такое произошло.
# Напишите програм-му, которая выводит на экран такую таблицу.

for a in range(0, 10, 1):
    for b in range(0, -10, -1):
        print(a+b, end='\t')
    print()