numbers = int(input('Кол-во чисел в списке: '))
numbers_list = []

for i in range(1, numbers + 1):
    num = int(input(f'Введите {i} число: '))
    numbers_list.append(num)

divider = int(input('\nВведите делитель: '))

index = 0
sum_indexes = 0
for number in numbers_list:
    if number % divider == 0:
        print(f"Индекс числа {number}: {index}")
        sum_indexes += index
    index += 1

print("Сумма индексов:", sum_indexes)