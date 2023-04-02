user_name = input('Введите имя: ')
debt_sum = int(input('Введите долг: '))

message = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}! {1} рублей где? А {0}?'.format(
    user_name,
    debt_sum
)

print(message)
