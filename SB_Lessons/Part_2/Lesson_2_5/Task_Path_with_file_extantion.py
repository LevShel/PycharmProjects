print('\nC:/user/docs/folder/new_file.txt\n')
user_name = input('Enter user name: ')
file_name = input('Enter file name: ')
path = f'C:/{user_name}/docs/folder/{file_name}'
if not path.endswith('.txt'):
    print('Error! Invalid file extention.')
else:
    print(path)