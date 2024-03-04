# Задача 1. Улучшенная лингвистика 2
# Усовершенствуйте старую программу:
# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст
# произведения, который вводится уже в одну строку. Напишите программу, которая посчитает,
# сколько раз слова пользователя встречаются в тексте.

words = input(f'Enter 3 comma-separated words: ')
text = input('Enter text: ')

searching_words = words.split(', ')
for word in searching_words:
    word_count = text.count(word)
    print(f'{word}: {word_count}')