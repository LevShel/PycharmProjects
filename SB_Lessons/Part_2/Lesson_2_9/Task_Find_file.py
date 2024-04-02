import os


def find_file(cur_path, file_name):
    print('\n step to ', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('\n \t view ', path)

        if file_name == i_elem:
            return path

        if os.path.isdir(path):
            print('\n this is dir')
            result = find_file(path, file_name)

            if result:
                break

        else:
            result = None

    return result


file_path = find_file(os.path.abspath(os.getcwd()), 'Task_Find_file.py')
if file_path:
    print('\n Absolute path: ', file_path)
else:
    print('\n File does not find.')