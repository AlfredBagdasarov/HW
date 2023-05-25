import os


def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == os.path.splitext(i_elem)[0]:
            print(os.path.abspath(path))
        if os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


search_in = input('Введите путь: ')
user_file_name = input('Введите имя файла: ')
file_path = find_file(search_in, user_file_name)
