def shell_sort(lst):
    n = len(lst)
    gap = n // 2  # Инициализация начального значения интервала
    while gap > 0:
        # Применяем сортировку вставками с заданным интервалом
        for i in range(gap, n):
            temp = lst[i]
            j = i
            # Сдвигаем элементы, чтобы найти правильную позицию для вставки элемента
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2  # Уменьшаем интервал
    return lst


# Пример использования
numbers = [8, 3, 1, 5, 2]
sorted_numbers = shell_sort(numbers)
print(sorted_numbers)  # Вывод: [1, 2, 3, 5, 8]
