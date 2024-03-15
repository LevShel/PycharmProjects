# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.
#
# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
#
# Содержимое файла answer.txt
# 20

file = open('numbers.txt', 'r')
nums = [int(num) for num in file]
file.close()

file = open('answer.txt', 'w')
file.write(str(sum(nums)))
file.close()