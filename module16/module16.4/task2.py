num_count = int(input('Кол-во участников: '))
mans_in_command = int(input('Кол-во человек в команде: '))

if num_count % mans_in_command == 0:
    all_commands = []
    num = 1
    for i in range(num_count // mans_in_command):
        all_commands.append(list(range(num, num + mans_in_command)))
        num += mans_in_command
    print(all_commands)
else:
    print(f'{num_count} участников невозможно поделить на команды по {mans_in_command} человек!')