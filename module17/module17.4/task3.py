import random

nums = int(input('Введите количество чисел: '))
numbers = [random.randint(-10, 10) for _ in range(nums)]

a_num = random.randint(0, len(numbers) - 2)
b_num = random.randint(a_num + 1, len(numbers) - 1)

print(numbers, a_num, b_num)
numbers = numbers[:a_num] + numbers[b_num + 1:]
print(numbers)
