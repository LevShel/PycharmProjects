# Задача 4. Уникальный шифр
# Контекст
# Представьте, что вы — детектив, который получил загадочное письмо с шифровкой. Нужно найти количество
# уникальных символов в письме, чтобы разгадать его и раскрыть тайну.
# Задача
# Напишите функцию, которая принимает строку и возвращает количество уникальных символов в строке.
# Используйте для выполнения задачи lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного регистра должны считаться одинаковыми.
# Советы
# Работать с регистрами помогут методы строк lower/upper.
# Уникальными считаются буквы, которые повторяются только один раз
# (например строка «аа» будет содержать 0 уникальных букв).
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5.

from collections import Counter


def count_unique_characters(text: str) -> int:
    counts = Counter(text.upper())
    counts = sum(1 for count in counts.values() if count == 1)
    return counts


message: str = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count: int = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
