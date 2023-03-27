left_limit = int(input('Левая граница: '))
right_limit = int(input('Правая граница: '))

cubes_list = [x ** 3 for x in range(left_limit, right_limit + 1)]
squares_list = [x ** 2 for x in range(left_limit, right_limit + 1)]

print(f'Список кубов чисел в диапазоне от {left_limit} до {right_limit}:', cubes_list)
print(f'Список квадратов  чисел в диапазоне от {left_limit} до {right_limit}:', squares_list)