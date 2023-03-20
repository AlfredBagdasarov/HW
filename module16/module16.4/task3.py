goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('Текущий ассортимент:', goods)

fruit_name = input('\nНовый фрукт: ')
price = int(input('Цена: '))
goods.append([fruit_name, price])
print('\nНовый ассортимент:', goods)

for price in goods:
    price[1] = round(price[1] * 1.08, 2)
print('\nНовый ассортимент с увел. ценой:', goods)