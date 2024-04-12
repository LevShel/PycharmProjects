# Задача 2. Случайная сумма
# Андрею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов. Каждый новый элемент —
# это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента (первый элемент — просто случайное
# вещественное число от 0 до 1). Андрею нельзя хранить в памяти весь этот список, а со значениями работать как-то
# надо.
# Помогите Андрею, реализуйте такой класс-итератор и проверьте его работу. Также сделайте, чтобы при каждом новом
# вызове итератора в цикле значения считались заново.
# Пример работы программы:
# Кол-во элементов: 5
# Элементы итератора:
# 0.74
# 1.13
# 1.95
# 2.2
# 2.55
# Новое кол-во элементов: 6
# Элементы итератора:
# 0.79
# 1.58
# 2.55
# 2.81
# 3.06
# 3.34

import random


class MyIterator:
    counter = 0

    def __init__(self, n):
        self.n = n
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter != self.n:
            self.current_num = self.current_num + random.random()
            self.counter += 1
            return round(self.current_num, 2)
        else:
            raise StopIteration


def my_generator():
    nums = int(input('Nums of elements: '))
    print('Elements of iterator: ')
    my_elms = MyIterator(nums)
    for i_elem in my_elms:
        print(i_elem)
    while True:
        nums = int(input('New nums of elements: '))
        print('Elements of iterator: ')
        my_elms = MyIterator(nums)
        for i_elem in my_elms:
            print(i_elem)


my_generator()