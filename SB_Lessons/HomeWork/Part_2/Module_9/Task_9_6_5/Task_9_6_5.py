# Задача 5. Частотный анализ
# Что нужно сделать
# Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет
# частотный анализ, определяя долю каждой буквы английского алфавита в общем количестве
# английских букв в тексте, и выводит результат в файл analysis.txt. Символы,
# не являющиеся буквами английского алфавита, учитывать не нужно.
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте,
# с тремя знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли.
# Буквы с равной долей должны следовать в алфавитном порядке.
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

file = open('text.txt', 'r')
text = file.read().lower()
file.close()

syms = sorted(set(sym for sym in text if sym.isalpha()))

dict_count_sym = {sym: text.count(sym) for sym in syms}

total_letters = sum(1 for sym in text if sym.isalpha())

for letter, num in dict_count_sym.items():
    dict_count_sym[letter] = round(1/total_letters*num, 3)

sorted_list_results = sorted(dict_count_sym.items(), key=lambda x: -x[1])

file = open('analysis.txt', 'w')
for letter, frequency in sorted_list_results:
    file.write(f'{letter} {frequency}\n')
file.close()
