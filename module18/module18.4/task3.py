string = input('Введите строку: ')
lowers = len([letter for letter in string if letter.islower()])
uppers = len([letter for letter in string if letter.isupper()])

if lowers > uppers:
    print('Результат:', string.lower())
else:
    print('Результат:', string.upper())
