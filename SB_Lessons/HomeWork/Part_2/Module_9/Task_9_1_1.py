# Задача 1. Сисадмин
# Вы работаете системным администратором в одной компании. На диске каждого
# сотрудника компании в специальной папке access лежит файл admin.bat.
# Этот файл предназначен для вас, и вам нужен путь до этого файла, причём как
# относительный, так и абсолютный. Недолго думая, вы решили написать небольшой скрипт,
# который закинете по сети к этому файлу.
# Напишите программу, которая выводит на экран относительный и абсолютный пути
# до файла admin.bat.
#
# Пример результата:
# Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
#
# Относительный путь до файла: Skillbox\access\admin.bat

import os

file_name = 'admin.bat'
folder_name = 'access'

abs_path = os.path.abspath(os.path.join('access', 'admin.bat'))
print('abs path: ', abs_path)

rel_path = os.path.relpath(abs_path)
print('rel path: ', rel_path)