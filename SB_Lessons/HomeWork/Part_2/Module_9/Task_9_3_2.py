# Задача 2. Поиск файла 2
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только
# программисту. Таким образом, с ними можно работать точно так же, как и с обычными
# текстовыми файлами.
# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая
# находит внутри указанного пути все файлы с искомым названием и выводит на экран
# текст одного из них (выбор можно сгенерировать случайно).
# Подсказка: можно использовать, например, список для сохранения найденного пути.

import os
import random

module = random.randint(1, 9)
lesson = random.randint(1, 9)
task = random.randint(1, 3)
file_name = f'Task_{module}_{lesson}_{task}.py'
dir_path = os.path.abspath(os.path.join('..', f'Module_{module}'))
curr_file = os.path.join(dir_path, file_name)

if os.path.exists(curr_file):
    print(f'\n File "{file_name}" in "Module {module}": \n')
    with open(curr_file, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)
else:
    print(f'\n File "{curr_file}" \n'
          f'does not exist.')
