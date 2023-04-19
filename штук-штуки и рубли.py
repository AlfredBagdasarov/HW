def func_psc(n):
    if 5 <= n % 100 <= 20:
        return f'{n} штук'
    elif n % 10 == 1:
        return f'{n} штука'
    elif n % 10 in (2, 3, 4):
        return f'{n} штуки'
    else:
        return f'{n} штук'


n = int(input())
print(func_psc(n))


def func_currency(n):
    if 5 <= n % 100 <= 20:
        return f'{n} рублей'
    elif n % 10 == 1:
        return f'{n} рубль'
    elif n % 10 in (2, 3, 4):
        return f'{n} рубля'
    else:
        return f'{n} рублей'


n = int(input())
print(func_currency(n))
