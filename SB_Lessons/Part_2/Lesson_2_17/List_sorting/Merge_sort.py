def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # Разделяем список на две половины
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Объединяем отсортированные половины в один список
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        # Сравниваем элементы из обоих списков и добавляем меньший в объединённый список
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Добавляем оставшиеся элементы из левого списка
    merged.extend(left[left_index:])
    # Добавляем оставшиеся элементы из правого списка
    merged.extend(right[right_index:])
    return merged


# Пример использования
numbers = [8, 3, 1, 5, 2]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Вывод: [1, 2, 3, 5, 8]
