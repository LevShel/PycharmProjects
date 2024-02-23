# Задача 2. Расшифровка кода
# Нам нужно расшифровать определённый код в виде одного большого числа.
# Для этого нужно посчитать сумму цифр справа налево.
# Если мы встречаем в числе цифру 5, то выводим сообщение «Обнаружен разрыв»
# и заканчиваем считать сумму. В конце программы на экран выводится сумма тех цифр,
# которые мы взяли.

import random

cipher = random.randint(9999999999, 99999999999999999999)
print('Ciphered message:\n', cipher)
last_num = cipher % 10
sum = last_num
next_nums = cipher // 10

while (next_nums % 10 != 5) and (next_nums - last_num != 0):
    last_num = next_nums % 10
    sum += last_num
    next_nums = next_nums // 10

print('Enciphered message:\n', sum)