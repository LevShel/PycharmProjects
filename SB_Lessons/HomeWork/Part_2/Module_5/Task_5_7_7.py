# Задание 7. IP-адрес 2
# Что нужно сделать
# При написании клиент-серверного приложения часто приходится работать с IP-адресами.
# Как вы уже знаете, IP-адрес состоит из четырёх целых чисел в диапазоне от 0 до 255,
# разделённых точками.
# Пользователь вводит строку. Напишите программу, которая определяет, действительно ли
# заданная строка — правильный IP-адрес. Обеспечьте контроль ввода, где предусматривается
# добавление целых чисел от 0 до 255 и точек между ними.
# Пример 1
# Введите IP: 128.16.35.a4
# a4 — это не целое число.
# Пример 2
# Введите IP: 240.127.56.340
# 340 превышает 255.
# Пример 3
# Введите IP: 34.56.42,5
# Адрес — это четыре числа, разделённые точками.
# Пример 4
# Введите IP: 128.0.0.255
# IP-адрес корректен.

def check_length(ip):
    if len(ip) == 4:
        return True
    else:
        return 'IP-address is 4 numbers, separated by dots.'


def check_range(ip):
    for part in ip:
        if not part.isdigit():
            return f'"{part}" isn`t a num.'
        elif not (0 <= int(part) <= 255):
            return f'"{part}" is out of range.'
    return True


inp_ip = input('>: ')
ip_address = inp_ip.split('.')
if (check_length(ip_address) is True and
        check_range(ip_address) is True):
    print(f'IP {'.'.join(ip_address)} is correct.')
else:
    print('Error!')
    if not check_length(ip_address) is True:
        print(check_length(ip_address))
    if not check_range(ip_address) is True:
        print({check_range(ip_address)})
