# Задание 7. Анализ слова — 2
# Что нужно сделать
# Продолжите писать анализаторы для текста. Теперь необходимо реализовать код,
# с помощью которого можно определять палиндромы, то есть слова, которые читаются
# одинаково слева направо и справа налево.
# Напишите такую программу.
# Пример 1:
# Введите слово: мадам
# Слово является палиндромом
# Пример 2:
# Введите слово: abccba
# Слово является палиндромом
# Пример 3:
# Введите слово: abbd
# Слово не является палиндромом

word = input('Enter word: ')
is_palindrome = True
for letter in range(len(word)//2):
    if word[letter] == word[len(word)-1-letter]:
        is_palindrome = True
    else:
        is_palindrome = False
        break
if is_palindrome:
    print('This word is palindrome.')
else:
    print('This word isn`t palindrome.')