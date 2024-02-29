# Задача 2. Вредоносное ПО
# Гера решил попрактиковаться в программировании и захотел написать небольшой скрипт,
# который после двух сообщений отправляет ещё одно на основе первых двух.
# Пользователь вводит две строки. В каждой из них есть какое-то количество специальных
# символов ! и ?. Напишите программу, которая считает количество этих символов отдельно
# в первой строке и отдельно во второй. Если в первой строке их больше, чем во второй,
# то на экран выводится первая строчка, объединённая со второй, а иначе — вторая с первой.
# При равном количестве символов в строках выводится «Ой».
#
# Пример 1:
# Первое сообщение: Привет!
# Второе сообщение: Как дела? Что делаешь?
#
# Третье сообщение: Как дела? Что делаешь? Привет!
#
# Пример 2:
# Первое сообщение: Хм!!
# Второе сообщение: ?
#
# Третье сообщение: Хм!!?

third_message = []
exclamation_mark = 0
question_mark = 0
for i in range(1, 2+1):
    input_message = input(f'{i} сообщение: ')
    exclamation_mark += input_message.count('!')
    question_mark += input_message.count('?')
    third_message.append(input_message)
for message in third_message:
    if message.count('!') > question_mark:
        third_message.remove(message)
        third_message.insert(0, message)
    elif message.count('?') > exclamation_mark:
        third_message.remove(message)
        third_message.insert(0, message)
print('3 сообщение: ', end='')
print(' '.join(third_message))
