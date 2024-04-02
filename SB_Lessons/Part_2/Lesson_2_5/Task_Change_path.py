user_name = input('Enter user name: ')
file_name = input('Enter file name: ')

path = 'C:/{user}/PycharmProjects/SB/SB_Lessons/Lesson_2_5_2/{new_file}.py'.format(
    user=user_name,
    new_file=file_name
)

path_2 = 'C:/{0}/PycharmProjects/SB/SB_Lessons/Lesson_2_5_2/{1}.py'.format(
    user_name,
    file_name
)

path_3 = f'C:/{user_name}/PycharmProjects/SB/SB_Lessons/Lesson_2_5_2/{file_name}.py'

print('\nPath v1: ', path)
print('Path v2: ', path_2)
print('Path v3: ', path_3)