# Задача 6. «Война и мир»
# Что нужно сделать
# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное
# произведение лежит в архиве voina-i-mir.zip. Напишите программу, которая подсчитывает
# статистику по буквам (не только русского алфавита) в этом романе и выводит результат
# на экран (или в файл). Результат должен быть отсортирован по частоте встречаемости букв
# (по возрастанию или убыванию). Регистр символов имеет значение.
# Архив можно распаковать вручную, но, если хотите, можете изучить документацию
# по модулю zipfile (можно использовать и другой модуль) и попробовать написать код,
# который будет распаковывать архив за вас.
import zipfile

with zipfile.ZipFile('voina_i_mir.zip', 'r') as myzip:
    files = myzip.namelist()
    with myzip.open(files[0], 'r') as file:
        text = file.read().decode('utf-8').upper()
file.close()
myzip.close()

syms = sorted(set(sym for sym in text if sym.isalpha()))
dict_count_sym = {sym: text.count(sym) for sym in syms}

sorted_list_results = sorted(dict_count_sym.items(), key=lambda x: -x[1])

file = open('letters_in_text.txt', 'w')
for letter, num in sorted_list_results:
    file.write(f'{letter} = {num}\n')
file.close()
