# Задание 5. Разворот
# Что нужно сделать
# На вход в программу подаётся строка, в которой буква h встречается как минимум два раза.
# Реализуйте код, который разворачивает последовательность символов, заключённую между
# первым и последним появлением буквы h, в противоположном порядке.
# Пример 1:
# Введите строку: hqwehrty
# Развёрнутая последовательность между первым и последним h: ewq.
# Пример 2:
# Введите строку: hh
# Развёрнутая последовательность между первым и последним h:
# Пример 3:
# Введите строку: hhqwerh
# Развёрнутая последовательность между первым и последним h: rewqh.

input_string = input('>: ')
print(input_string[input_string.rindex('h')-1:input_string.index('h'):-1])