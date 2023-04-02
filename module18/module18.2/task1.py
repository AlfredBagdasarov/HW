user_name = input('Имя: ')
order_num = int(input('Номер заказа: '))

message = 'Здравствуйте, {name}! Ваш номер заказа: {order}. Приятного дня!'.format(
    name=user_name,
    order=order_num
)
print(message)
