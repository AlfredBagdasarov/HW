left_limit = int(input('Левая граница: '))
right_limit = int(input('Правая граница: '))

evens_list = [x for x in range(left_limit, right_limit + 1) if x % 2 == 0]

print(f'Список четных чисел в диапазоне от {left_limit} до {right_limit}:', evens_list)