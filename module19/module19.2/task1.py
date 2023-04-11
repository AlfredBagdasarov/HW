small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)
name_item = input('Введите название товара: ')

if big_storage.get(name_item):
    print(name_item, ':', big_storage[name_item])
else:
    print('Ошибка: такого товара нет на складе.')
