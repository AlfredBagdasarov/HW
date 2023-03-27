string = input('Введите строку: ')
add_sym = input('Введите дополнительный символ: ')

double_sym_list = [x * 2 for x in string]
add_sym_list = [x + add_sym for x in double_sym_list]

print('Список удвоенных символов:', double_sym_list)
print('Склейка с дополнительным символом:', add_sym_list)