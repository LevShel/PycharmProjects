# Задача 3. Кастомные исключения
# Исключения в Python также являются классами, и все они берут свои истоки
# от самого главного класса — Exception. И для создания своего собственного класса
# ошибки достаточно написать его дочерний класс. Например:
class MyOwnException(Exception):
    pass


# raise MyOwnException('Это моя ошибка!')
# Причём содержимое объекта исключения чаще всего так и оставляют (просто pass),
# чтобы не сломать автоматические обработчики исключений.
# Напишите программу, которая считывает из файла numbers.txt пары чисел, делит первое
# число на второе и выводит ответ на экран. Если первое число меньше второго,
# то программа выдаёт исключение DivisionError (нельзя делить меньшее на большее).
# Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.

with open('numbers.txt', 'r') as file:
    nums = file.readlines()

if int(nums[0]) < int(nums[1]):
    raise MyOwnException('Нельзя делить меньшее на большее.')
else:
    print(int(nums[0]) / int(nums[1]))