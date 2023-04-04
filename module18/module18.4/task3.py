string = input('Введите строку: ')
lowers = len([letter for letter in string if letter.islower()])
uppers = len([letter for letter in string if letter.isupper()])

if lowers > uppers:
    print(string.lower())
else:
    print(string.upper())
