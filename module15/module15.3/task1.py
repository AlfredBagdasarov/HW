string = input('Введите строку: ')
text_list = list(string)
count = 0

print('Исправленная строка: ', end='')
for sym in text_list:
    if sym == ':':
        sym = ';'
        count += 1
    print(sym, end='')
print('\nКол-во замен:', count)