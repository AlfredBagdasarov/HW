order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

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

total_sum = [i_fruit if incomes.get(i_fruit) == order.get(i_fruit)
             else incomes.get(i_fruit, 0) * order[i_fruit] for i_fruit in order]
print('Итоговая стоимость товаров из заказа составляет:', sum(total_sum))
