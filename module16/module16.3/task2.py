first_string = input('Первое сообщение: ')
second_string = input('Второе сообщение: ')
first_count = first_string.count('!') + first_string.count('?')
second_count = second_string.count('!') + second_string.count('?')

if first_count < second_count:
    first_string, second_string = second_string, first_string
elif first_count == second_count:
    print('\nОй')
print('\nТретье сообщение:', first_string + second_string)