contact_dict = dict()

while True:
    print('Текущие контакты на телефоне:')
    if contact_dict:
        for name in contact_dict:
            print(name, contact_dict[name])
    else:
        print('<Пусто>')
    name = input('\nВведите имя: ')
    tel_number = input('Введите номер телефона: ')
    if name in contact_dict:
        print('Ошибка: такое имя уже существует.')
        break
    else:
        contact_dict[name] = tel_number
