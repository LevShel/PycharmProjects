# Задача 3.
# Мы входим в команду разработки нового текстового редактора и нам поручили
# разработать для него под-счёт нужного символа в тексте, а именно - буквы Ы.
# Причём отдельно с верхним регистром и отдельно с нижним.
# Напишите программу, которая считает количество больших и количество маленьких
# букв Ы в тексте и выво-дит ответ на экран.
# Пример:
# Введите текст: Прыг скок
# Больших букв Ы: 0
# Маленьких букв Ы: 1

text = input('Enter text: ')
big_letter = 'Y'
big_letter_count = 0
little_letter = 'y'
little_letter_count = 0
for sym in text:
    if sym == big_letter:
        big_letter_count += 1
    elif sym == little_letter:
        little_letter_count += 1
print(f'Big letters "{big_letter}": {big_letter_count}')
print(f'Little letters "{little_letter}": {little_letter_count}')