# Задание 9. Обратный анализ чётных чисел
# Контекст
# Вы работаете в научной лаборатории, в ней проводятся эксперименты и записываются
# результаты в виде списка целых чисел. Ваша задача — написать программу, которая
# поможет исследователям выделить чётные числа из списка результатов экспериментов.
# Они хотят анализировать эти числа в обратном порядке, чтобы исследовать особые
# закономерности, связанные с чётными значениями.
# Задача
# Напишите программу, которая считывает целые числа из списка и выводит из него только
# чётные в обратном порядке. Создавать дополнительные списки нельзя.r
# Ограничения
# Нельзя использовать:
# •	метод reverse,
# •	функцию reversed,
# •	разворот при помощи среза (список[::-1]).
# Советы
# •	Вы можете управлять направлением перебора элементов в списке (можете перебирать
# элементы с начала до конца, а можете начать с конца и двигаться к началу).
# Это может стать основой решения задачи.
# •	Список является изменяемым типом данных, значит вы можете изменять положение
# элементов внутри списка. Это может стать основой ещё одного варианта решения задачи.
# Можете выбрать любой или решить обоими способами!
# •	Обратите внимание: некоторые операции со списками создают их копии, даже если
# вы не указываете на это явно. Простой пример, который это демонстрирует:
# test = [1, 2, 3]
# print(id(test)) # Здесь вы увидите один айди
# test = test[::-1]
# print(id(test)) # А здесь уже другой

test_results = [4, 8, 15, 16, 23, 42]
for i in range(len(test_results)-1, 0, -1):
    if test_results[i] % 2 == 0:
        print(test_results[i], end=', ')