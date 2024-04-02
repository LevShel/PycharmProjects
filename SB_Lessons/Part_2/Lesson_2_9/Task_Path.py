import os

folder_name = 'project'
file_name = 'my_file.txt'

path = 'docs/{folder}/{file}'.format(
    folder=folder_name,
    file=file_name)
print(path)

rel_path = os.path.join('docs', folder_name, file_name)
print(rel_path)

abs_path = os.path.abspath(file_name)
print(abs_path)