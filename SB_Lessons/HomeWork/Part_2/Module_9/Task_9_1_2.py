# Задача 2. Содержимое
# Выберите любую директорию на своём диске и затем напишите программу,
# выводящую на экран абсолютные пути к файлам и папкам, которые находятся
# внутри этой директории.
#
# Результат программы на примере директории проекта python_basic:
# Содержимое каталога G:\PycharmProjects\python_basic
#     G:\PycharmProjects\python_basic\.git
#     G:\PycharmProjects\python_basic\.idea
#     G:\PycharmProjects\python_basic\Module14
#     G:\PycharmProjects\python_basic\Module15
#     G:\PycharmProjects\python_basic\Module16
#     G:\PycharmProjects\python_basic\Module17
#     G:\PycharmProjects\python_basic\Module18
#     G:\PycharmProjects\python_basic\Module19
#     G:\PycharmProjects\python_basic\Module20
#     G:\PycharmProjects\python_basic\Module21
#     G:\PycharmProjects\python_basic\Module22

import os


def print_dirs(project):
    print('\nDirectory: ', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('\t', path)


project_dir = 'SB'
path_to_project = os.path.abspath(os.path.join('..', '..', '..', '..', '..', project_dir))
print_dirs(path_to_project)
