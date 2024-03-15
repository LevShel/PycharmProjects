# Задача 1. Сумма чисел 2
# Что нужно сделать
# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены
# пробелами и концами строк. Напишите программу, которая выводит сумму чисел во выходной
# файл answer.txt.
# Пример:
# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2
# Содержимое файла answer.txt
# 8

file = open('numbers.txt', 'r')
nums = [int(i_str.replace(' ', '')) for i_str in file]
file.close()

file = open('answer.txt', 'w')
file.write(str(sum(nums)))
file.close()