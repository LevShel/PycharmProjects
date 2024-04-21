def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Сравниваем пару соседних элементов
            if lst[j] > lst[j + 1]:
                # Если элементы находятся в неправильном порядке, меняем их местами
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    # Пример использования


numbers = [5, 3, 8, 2, 1]
bubble_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]
