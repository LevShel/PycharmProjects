# Задача 6. Полёт
# Что нужно сделать
# Напишите программу для сервиса заказа билетов, которая запрашивает
# у пользователя город вылета и город прилёта. Затем выведите их в одну строку
# через тире. Обратите внимание на свои переменные: названия должны отражать содержимое.
#
# Что оценивается
# •	input содержит корректное приглашение для ввода: “input()” — неверно;
# •	результат вывода соответствует заданию;
# •	переменные имеют значащие имена, не только a, b, c, d (видео 2.3);
# •	пробелы после запятых, пробелы при бинарных операциях (конкатенация в данной задаче);
# •	после запятой стоит пробел, перед запятой пробела нет;
# •	отсутствуют пробелы после print и перед скобками: “print ()” — неверно, “print()” — верно;
# •	нет пробелов и внутри скобок.

name_of_programm = 'Aviasales'
print('+', '-'*(len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-'*(len(name_of_programm)-8), 'by ШелЛ +\n')

dep_city = input('Departure from: ')
arr_city = input('Arrival to: ')

print('Searching fligts {departure} - {arrival}...'.format(departure=dep_city, arrival=arr_city))