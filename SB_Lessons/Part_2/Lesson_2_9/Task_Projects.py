import os


def print_dirs(project):
    print('\nDirectory: ', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('\t', path)


projects_list = ['SB_Lessons', 'Memory_stiks']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join('../..', '..', i_project))
    print_dirs(path_to_project)
