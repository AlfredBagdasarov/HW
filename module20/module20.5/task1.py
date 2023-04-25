data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}


def is_info(ser_and_num, dictionary):
    if ser_and_num in dictionary:
        print(dictionary[series_and_number][0], dictionary[series_and_number][1])
    else:
        print('Такого человека нет в базе данных.')


series = int(input('Введите серию паспорта: '))
number = int(input('Введите номер паспорта: '))
series_and_number = series, number
is_info(series_and_number, data)
