contact_dict = dict()

while True:
    print('Текущие контакты на телефоне:')
    if contact_dict:
        for i_info in contact_dict:
            print(f'{i_info[0]} {i_info[1]}: {contact_dict[i_info]}')
    else:
        print('<Пусто>')
    name = input('\nВведите имя: ')
    surname = input('Введите фамилию: ')
    full_name = surname, name
    if full_name not in contact_dict:
        contact_dict[full_name] = int(input('Введите номер телефона: '))
    else:
        print('Ошибка: такое имя уже существует.')
        break
