# Задание 1. Страшный код
# Что нужно сделать
# Вашему другу, который тоже начал изучать Python, преподаватель дал такую задачу:
# есть один основной (‘a’) и два побочных списка (‘b’ и ‘c’), в основном лежат
# элементы [1, 5, 3], а в побочных — [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.
# Программа добавляет элементы побочного списка ‘b’ в основной, а затем считает
# количество цифр 5. Это число выводится на экран, и после этого цифры 5 удаляются
# из основного списка. Затем программа добавляет в основной список элементы списка ‘c’,
# считает количество цифр 3 и выводит это число на экран. В конце появляется и сам список.
# Вот сам код:
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
# a.append(i)
# t = 0
# for i in a:
# if i == 5:
# t += 1
# print(t)
# d = []
# for i in a:
# if i != 5:
# d.append(i)
# for i in c:
# d.append(i)
# t = 0
# for i in d:
# if i == 3:
# t += 1
# print(t)
# print(d)
# Используя знания о методах списков, а также о стиле программирования,
# помогите другу переписать программу. Не используйте дополнительные списки.
# Результат работы программы:
# Количество цифр 5 при первом объединении: 3
# Количество цифр 3 при втором объединении: 4
# Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]

def count_digits(spisok, digit):
    digits = spisok.count(digit)
    return digits


def delete_digits(spisok, digit):
    for i in spisok:
        if i == digit:
            spisok.remove(i)
    return spisok


a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

for i in b:
    a.append(i)
    current_digit = 5
print(f'There are {count_digits(a, current_digit)} digits {current_digit} '
      f'after first combined.')
delete_digits(a, current_digit)

for j in c:
    a.append(j)
    current_digit = 3
print(f'There are {count_digits(a, current_digit)} digits {current_digit} '
      f'after first combined.')

print(f'Final list: {a}')