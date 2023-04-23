import random


def gen_random_letter(count):
    return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=count)


first_list = gen_random_letter(10)
second_list = gen_random_letter(10)
print('Первый список:', first_list)
print('Второй список:', second_list)

first_dict = dict(enumerate(first_list))
second_dict = dict(enumerate(second_list))
print('\nПервый словарь:', first_dict)
print('Второй словарь:', second_dict)
