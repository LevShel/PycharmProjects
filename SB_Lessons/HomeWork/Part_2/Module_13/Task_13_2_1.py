# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая эмулирует работу цикла for
# с помощью цикла while и проходит во всем элементам итерируемого объекта. Не забудьте про исключение «конца итерации».

""" MY VERSION: """


def my_for(any_object):
    n = len(any_object)
    i = 0
    while i != n:
        print(any_object[i], end='\n')
        i += 1


my_list = [4, 8, 15, 16, 23, 42]
my_for(my_list)

""" CHAT GPT: """


def custom_for(any_object):
    iterator = iter(any_object)  # Получаем итератор из итерируемого объекта
    try:
        while True:
            element = next(iterator)  # Получаем следующий элемент итератора
            print(element)  # Делаем что-то с текущим элементом
    except StopIteration:  # Исключение "конца итерации": просто завершаем цикл
        pass


my_list = [4, 8, 15, 16, 23, 42]
custom_for(my_list)
