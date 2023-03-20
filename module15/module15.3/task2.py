string = input('Введите строку: ')
num_sym_in_string = int(input('Номер символа: ')) - 1
string_list = list(string)
count = 0

if string_list[num_sym_in_string] == string_list[num_sym_in_string - 1]:
    print('\nСимвол слева:', string_list[num_sym_in_string - 1])
    count += 1
elif string_list[num_sym_in_string] == string_list[num_sym_in_string + 1]:
    print('Символ справа:', string_list[num_sym_in_string + 1])
    count += 1

if count == 0:
    print('\nТаких же символов нет.')
elif count == 1:
    print('\nЕсть ровно один такой же символ.')
else:
    print('\nТаких символов два.')