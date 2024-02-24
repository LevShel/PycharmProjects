# Задание 6. Бегущие цифры
# Что нужно сделать
# Вы пишете программу для маленького табло, в котором циклически повторяется один
# и тот же текст или числа, например как в метро, автобусах или трамваях.
# Дан список из N элементов и целое число K. Напишите программу, которая циклически
# сдвигает элементы списка вправо на K позиций. Используйте минимально возможное
# количество операций присваивания.
# Пример 1:
# Сдвиг: 1
# Изначальный список: [1, 2, 3, 4, 5]
# Сдвинутый список: [5, 1, 2, 3, 4]
# Пример 2:
# Сдвиг: 3
# Изначальный список: [1, 4, –3, 0, 10]
# Сдвинутый список: [–3, 0, 10, 1, 4]

# start_list = [1, 2, 3, 4, 5]
# new_list = []
# shift = int(input('Enter shift: '))
# for i in start_list:
#     new_list.append(i)
# new_list = new_list[shift:]
# for j in start_list:
#     if start_list.index(j) == 0:
#         new_list.append(j)
# print(f'The original list: {start_list}')
# print(f'Shifted list: {new_list}')

start_list = [1, 2, 3, 4, 5]
shift = int(input('Enter shift: '))
n = len(start_list)
shift %= n

start_list[:] = start_list[-shift:] + start_list[:-shift]

print('Shifted list:', start_list)
