# Задача 4. Информация о пользователе
# Что нужно сделать
# Напишите программу, которая запрашивает некоторые данные у пользователя,
# затем выведите их на экран, как показано ниже. Данные должны лежать в разных переменных.
#
# Вариант 1. Запросите имя и фамилию и выведите их на экран построчно.
# Результат должен быть таким (с вашим именем и фамилией, конечно):
#
#
# Вариант 2. Запросите имя, фамилию и город проживания, затем выведите их на экран в две строки:
# первая — «Вас зовут» и далее имя и фамилия, вторая — «Вы живёте в городе» и далее город.
# Для красоты отделите в консоли ввод и вывод данных,
# как в примере:
#
#
# Что оценивается
# •	input содержит корректное приглашение для ввода: “input()” — неверно;
# •	результат вывода соответствует примеру;
# •	переменные имеют значащие имена, не только a, b, c, d (видео 2.3);
# •	пробелы после запятых, пробелы при бинарных операциях;
# •	после запятой стоит пробел, перед запятой пробела нет;
# •	отсутствие пробелов после print и перед скобками: “print ()” — неверно, “print()” — верно;
# •	отсутствуют пробелы внутри скобок.

name = input('Enter yor name: ')
surname = input('Enter your surname: ')
city = input('Enter your city: ')
print('==========')
print('You are ', name, surname)
print('You live in ', city)