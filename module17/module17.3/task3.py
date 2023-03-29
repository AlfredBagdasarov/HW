def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)


prices_list = [float(input('Цена на товар: ')) for _ in range(5)]
first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))

prices_first_year = [get_higher_price(first_percent, i_price) for i_price in prices_list]
prices_second_year = [get_higher_price(second_percent, i_price) for i_price in prices_first_year]

print(f'Сумма цен за каждый год: {round(sum(prices_list), 2)}, {round(sum(prices_first_year), 2)}, {round(sum(prices_second_year), 2)}')