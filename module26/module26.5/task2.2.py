with open('numbers.txt', 'w', encoding='utf-8') as file:
    for i in range(0, 1000001):
        file.write('{} '.format(i))
