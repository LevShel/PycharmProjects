def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]  # Берём текущий элемент, который нужно вставить в отсортированную часть списка
        j = i - 1
        # Перемещаем элементы, которые больше key, на одну позицию вперёд
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key  # Вставляем key в правильное место


# Пример использования
numbers = [5, 3, 8, 2, 1]
insertion_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]
