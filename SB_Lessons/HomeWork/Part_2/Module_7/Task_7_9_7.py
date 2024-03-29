# Задача 7. Своя функция zip
# Что нужно сделать
# В самом конце собеседования вам неожиданно сказали: «Расскажите, что делает функция zip».
# Чтобы произвести впечатление, вы решили не только рассказать о ней, но и написать
# её аналог.
# Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор
# из пар кортежей «символ — число». Затем выведите на экран сам генератор и кортежи.
# Пример:
# Строка: abcd
# Кортеж чисел: (10, 20, 30, 40)
# Результат:
# <generator object <genexpr> at 0x00000204A4234048>
# ('a', 10)
# ('b', 20)
# ('c', 30)
# ('d', 40)
# Дополнительно: создайте полный аналог функции zip — сделайте так, чтобы программа
# работала с любыми итерируемыми типами данных.
# Подсказка
# Ранее мы проходили List comprehensions — по сути, генератор списка. В этом случае,
# чтобы создать генератор, попробуйте поэкспериментировать с генератором списка.

string_original = 'abcd'
tuple_original = (10, 20, 30, 40)
print()
print(zip(string_original, tuple_original))
zip_list = [(i, j) for
            idx_tpl, j in enumerate(tuple_original) for
            idx_str, i in enumerate(string_original) if
            idx_str == idx_tpl]
zip_tuple = ((i, j) for
            idx_tpl, j in enumerate(tuple_original) for
            idx_str, i in enumerate(string_original) if
            idx_str == idx_tpl)
print('\n'.join(map(str, zip_list)))
print(zip_tuple)

