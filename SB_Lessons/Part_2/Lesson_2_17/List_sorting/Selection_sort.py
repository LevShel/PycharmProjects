def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        # Находим индекс минимального элемента в неотсортированной части списка
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        # Меняем местами минимальный элемент с первым элементом неотсортированной части
        lst[i], lst[min_index] = lst[min_index], lst[i]


# Пример использования
numbers = [5, 3, 8, 2, 1]
selection_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]
