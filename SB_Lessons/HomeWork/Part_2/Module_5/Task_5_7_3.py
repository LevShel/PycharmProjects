# Задание 3. Файлы
# Что нужно сделать
# В IT-компании есть негласные правила именования текстовых документов:
# 1.	Название файла не может начинаться с одного из специальных символов:
# @, №, $, %, ^, &, *, ().
# 2.	Файл должен заканчиваться расширением .txt или .docx.
# Напишите программу, которая получает на вход полное название файла и проверяет,
# соответствует ли он этим правилам.
# Пример 1
# Название файла: @example.txt.
# Ошибка: название начинается недопустимым символом.
# Пример 2
# Название файла: example.ttx.
# Ошибка: неверное расширение файла. Ожидалось .txt или .docx.
# Пример 3
# Название файла: example.txt.
# Файл назван верно.

special_symbols = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
true_extensions = ['.txt', '.docx']

file_name = input('>: ')
if any(file_name.startswith(symbol) for symbol in special_symbols):
    print('Wrong name of file.')
elif not any(file_name.endswith(symbol) for symbol in true_extensions):
    print('Wrong extension of file.')
else:
    print('File name is true.')
    