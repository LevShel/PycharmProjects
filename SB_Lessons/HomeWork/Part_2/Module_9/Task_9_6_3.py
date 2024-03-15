# Задача 3. Файлы и папки
# Что нужно сделать
# Напишите программу, которая получает на вход путь до каталога
# (в том числе это может быть просто корень диска) и выводит общее количество файлов
# и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах
# (1 килобайт = 1024 байт).
# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров
# всех вложенных в него файлов.
# Результат работы программы на примере python_basic\Module14:
# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кбайтах): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15

import os


def calculate_dir_size(dir_path):
    total_size = 0
    total_files = 0
    total_dirs = 0

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
            total_files += 1
        total_dirs += len(dirs)

    total_size_kb = total_size / 1024
    return total_size_kb, total_files, total_dirs


dir_path = os.path.abspath(os.path.join('.'))
print(f'\n "{dir_path}":')
size_kb, files_count, dirs_count = calculate_dir_size(dir_path)
print(f'Размер каталога (в Кбайтах): {size_kb}')
print(f'Количество подкаталогов: {dirs_count}')
print(f'Количество файлов: {files_count}')
