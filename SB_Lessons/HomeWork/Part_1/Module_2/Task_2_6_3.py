# Задача 3. Животные
# Что нужно сделать
# Создайте две переменные с именами «Первое животное» и «Второе животное» на английском языке.
# Запишите в первую переменную слово «Заяц», а во вторую — «Черепаха».
# Используя эти переменные, выведите на экран текст «Заяц спит, Черепаха идёт» в одну строку.
#
# Что оценивается
# •	input содержит корректное приглашение для ввода: “input()” — неверно;
# •	переменные имеют значащие имена, не только a, b, c, d (видео 2.3);
# •	после запятой стоит пробел, перед запятой пробела нет;
# •	отсутствие пробелов после print и перед скобками: “print ()” — неверно, “print()” — верно.

first_animal = 'Rabbit'
second_animal = 'Turtle'

print('{} is sleeping, {} is going.'.format(first_animal, second_animal))