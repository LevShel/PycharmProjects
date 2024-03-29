# Задание 4. Тренировка со срезами
# Что нужно сделать
# Дана строка, в которой хранятся первые семь букв английского алфавита.
# alphabet = 'abcdefg'
# Напишите программу, которая выводит на экран десять таких результатов:
# 1.	копию строки;
# 2.	элементы строки в обратном порядке;
# 3.	каждый второй элемент строки (включая самый первый);
# 4.	каждый второй элемент строки после первого;
# 5.	все элементы до второго;
# 6.	все элементы, начиная с конца до предпоследнего;
# 7.	все элементы в диапазоне индексов от 3 до 4 (не включая 4);
# 8.	последние три элемента строки;
# 9.	все элементы в диапазоне индексов от 3 до 4;
# 10.	то же, что и в предыдущем пункте, но в обратном порядке.
# Для получения и вывода результатов используйте только команду print и срезы.
# Результаты работы программы:
# 1: abcdefg
# 2: gfedcba
# 3: aceg
# 4: bdf
# 5: a
# 6: g
# 7: d
# 8: efg
# 9: de
# 10: ed

alphabet = 'abcdefg'
print(f'1:\t {alphabet[::]}')
print(f'2:\t {alphabet[::-1]}')
print(f'3:\t {alphabet[::2]}')
print(f'4:\t {alphabet[1::2]}')
print(f'5:\t {alphabet[:1:]}')
print(f'6:\t {alphabet[-1::]}')
print(f'7:\t {alphabet[3:4:]}')
print(f'8:\t {alphabet[-3::]}')
print(f'9:\t {alphabet[3:5:]}')
print(f'10:\t {alphabet[4:2:-1]}')
