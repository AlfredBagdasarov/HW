ip_address = '{0}.{1}.{2}.{3}'
numbers = []

while len(numbers) != 4:
    ip_num = int(input('Введите число в диапазоне от 0 до 255 (включительно): '))
    if 0 <= ip_num <= 255:
        numbers.append(ip_num)
    else:
        print('Ошибка ввода. Число должно быть в диапазоне от 0 до 255 (включительно).')

print(ip_address.format(*numbers))
