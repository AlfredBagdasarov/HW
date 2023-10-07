def func_2(func, number):
    return func(number) * func(number)


def func_1(x):
    return x + 10


print('Результат:', func_2(func_1, 9))
