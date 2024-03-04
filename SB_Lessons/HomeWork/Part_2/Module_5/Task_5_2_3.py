# Задача 3. IP-адрес
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой. Каждое число находится
# в диапазоне от 0 до 255 (включительно).
#
# Пример правильного адреса: 192.168.1.0
# Пример неправильного адреса: 192.168.300.0
#
# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес.
# Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.

ip_part_1 = int(input('>: '))
if 0 > ip_part_1 > 255:
    print('Error! Enter num in range 0...255.')
    ip_part_1 = int(input('>: '))
else:
    ip_part_2 = int(input('>: '))
    if 0 > ip_part_2 > 255:
        print('Error! Enter num in range 0...255.')
        ip_part_1 = int(input('>: '))
    else:
        ip_part_3 = int(input('>: '))
        if 0 > ip_part_3 > 255:
            print('Error! Enter num in range 0...255.')
            ip_part_1 = int(input('>: '))
        else:
            ip_part_4 = int(input('>: '))
            if 0 > ip_part_4 > 255:
                print('Error! Enter num in range 0...255.')
                ip_part_4 = int(input('>: '))
            else:
                print(f'{ip_part_1}.{ip_part_2}.{ip_part_3}.{ip_part_4}')
