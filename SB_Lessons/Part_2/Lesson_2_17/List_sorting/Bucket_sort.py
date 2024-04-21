def bucket_sort(lst):
    # Определяем количество карманов
    num_buckets = len(lst)
    # Создаём пустые карманы
    buckets = [[] for _ in range(num_buckets)]
    # Распределяем элементы по карманам
    for num in lst:
        index = int(num * num_buckets)  # Вычисляем индекс кармана для текущего элемента
        buckets[index].append(num)
    # Сортируем каждый карман отдельно
    for bucket in buckets:
        bucket.sort()
    # Объединяем элементы из всех карманов
    sorted_lst = []
    for bucket in buckets:
        sorted_lst += bucket
    return sorted_lst


# Пример использования
numbers = [0.42, 0.25, 0.75, 0.12, 0.9]
sorted_numbers = bucket_sort(numbers)
print(sorted_numbers)  # Вывод: [0.12, 0.25, 0.42, 0.75, 0.9]
