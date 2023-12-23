numbers: str = input('Введите числа (через пробел): ')
print(sorted(list(map(int, numbers.split()))))
