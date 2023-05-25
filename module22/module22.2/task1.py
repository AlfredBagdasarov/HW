import os

path_to = input('Введите путь: ')

if os.path.isdir(path_to):
    print('Это папка!')
elif os.path.isfile(path_to):
    print('Это файл')
    print('Размер файла:', os.path.getsize(path_to), 'байт')
elif os.path.islink(path_to):
    print('Это ссылка')
else:
    print('Указанного пути не существует.')
