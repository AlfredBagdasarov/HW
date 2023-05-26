import os
import random


def find_file(cur_path, file_name):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == os.path.splitext(i_elem)[0]:
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                all_paths.extend(result)

    return all_paths


def check_file_inside(path_to_file):
    file = open(path_to_file, 'r', encoding='utf-8')
    for i_line in file:
        print(i_line, end='')
    file.close()


search_in = input('Введите путь: ')
user_file_name = input('Введите имя файла: ')
file_path = find_file(search_in, user_file_name)
check_file_inside(random.choice(file_path))
