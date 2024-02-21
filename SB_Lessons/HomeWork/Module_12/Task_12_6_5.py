# Задача 5. Текстовый редактор
# Что нужно сделать
# Продолжаем разрабатывать новый текстовый редактор. В этот раз нам поручили написать
# для него код, который считает, сколько раз в тексте встречается любая выбранная
# буква или цифра (а не только буквы Ы, как раньше).
# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N. Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определённом формате.
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? Л
# Количество цифр 0: 2
# Количество букв Л: 1

def count_letters(input_text):
    digits = input("Какую цифру ищем? ")
    letters = input("Какую букву ищем? ")

    count_digit = input_text.count(digits)
    count_letter = input_text.lower().count(letters.lower())

    print(f"Количество цифр {digits}: {count_digit}")
    print(f"Количество букв {letters}: {count_letter}")


text = input("Введите текст: ")
count_letters(text)
