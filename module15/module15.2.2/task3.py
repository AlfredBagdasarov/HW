numbers_list = []
numbers_count = int(input('Кол-во чисел в списке: '))

for _ in range(numbers_count):
    num = int(input('Очередное число: '))
    numbers_list.append(num)

if numbers_list:
    maximum = numbers_list[0]
    minimum = numbers_list[0]
    minimum_index = 0
    maximum_index = 0

    for i in numbers_list:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i
    for index in numbers_list:
        if maximum < index:
            maximum_index = index
        if minimum > index:
            minimum_index = index
    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)
    print(numbers_list)
    numbers_list[minimum_index], numbers_list[maximum_index] = numbers_list[maximum_index], numbers_list[minimum_index]
    print(numbers_list)
else:
    print('В списке нет чисел!')