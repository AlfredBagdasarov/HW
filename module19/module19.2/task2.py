incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

total_sum = 0
min_value = None
min_name = ''
for name, value in incomes.items():
    total_sum += value
    if min_value is None or min_value > value:
        min_value = value
        min_name = name

incomes.pop(min_name)

print(f'Общий доход за год составил {total_sum} рублей')
print(f'Самый маленький доход у {min_name}. Он составляет {min_value} рублей')
print('Итоговый словарь:', incomes)

# Вариант решения с "магией":
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
def get_value(x):
    return x[1]

result_sum = sum(incomes.values())
min_name, min_value = min(incomes.items(), key=get_value)
# При помощи функции и параметра key мы говорим пайтону как именно надо сравнивать между собой элементы
# Т.к. элементы записаны в таком виде - ('apple': 5600.20), а сравнивать мы хотим по значениям - то нам проосто надо брать для сравнения
# элементы под индексом 1 (если бы сравнивали по ключам, то индекс надо было бы заменить на 0)
print(f'\nОбщий доход за год составил {total_sum} рублей')
print(f'Самый маленький доход у {min_name}. Он составляет {min_value} рублей')
print('Итоговый словарь:', incomes)
