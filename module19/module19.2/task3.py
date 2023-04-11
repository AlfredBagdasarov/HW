text = input('Введите текст: ')
hist = dict()

for sym in text:
    if sym in hist:
        hist[sym] += 1
    else:
        hist[sym] = 1

for letter, freq in hist.items():
    print(letter, ':', freq)

print('Максимальная частота:', max(hist.values()))
