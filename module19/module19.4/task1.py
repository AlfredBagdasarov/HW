string = set(input('Введите строку: '))
symbols = set('.,;:!?')
print('Количество знаков пунктуации:', len(string.intersection(symbols)))
