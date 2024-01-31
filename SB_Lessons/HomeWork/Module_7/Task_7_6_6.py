# Задача 6. Замечательные числа
# Что нужно сделать
# Напишите программу, которая находит и выводит все двузначные числа,
# равные утроенному произведению своих цифр. К таким относятся,
# например, 15 и 24.

for num in range (10,100):
    first_number = num // 10
    second_number = num % 10
    triple_prod = first_number * second_number * 3
    if triple_prod == num:
        print(f'{first_number} x {second_number} x 3 = {num}')