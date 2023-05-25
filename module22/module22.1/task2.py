import os


def print_dirs(project):
    print('\nСодержимое каталога:', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('\t', path)


project_list = ['HW', 'Python_Basic']
for i_project in project_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', '..', i_project))
    print_dirs(path_to_project)

for path in os.listdir('..'):
    print(os.path.join(os.path.abspath('..'), path))
