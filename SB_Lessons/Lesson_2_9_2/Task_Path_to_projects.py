import os


def print_dirs(project):
    print('\nDirectory: ', project)
    if os.path.exists(project):
        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)
            print('\t', path)
    else:
        print('Dir does not exists.')


projects_list = ['SB_Lessons', 'Production']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)
