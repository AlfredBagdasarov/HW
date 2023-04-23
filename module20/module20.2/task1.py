import random


def create_random_tuple(num_1, num_2, range_num):
    return tuple(random.randint(num_1, num_2) for _ in range(range_num))


first_tuple = create_random_tuple(0, 5, 10)
second_tuple = create_random_tuple(-5, 0, 10)
third_tuple = first_tuple + second_tuple
print(third_tuple)
print('Кол-во нулей в 3-ем кортеже:', third_tuple.count(0))
