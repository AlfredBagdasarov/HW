path = input('Введите путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
file_extension = input('Требуемое расширение файла: ')

if path.startswith(disk) and path.endswith(file_extension):
    print('Путь корректен!')
else:
    print('Ошибка: неверное расширение файла или неверно указан диск.')
