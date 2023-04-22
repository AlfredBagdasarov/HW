import math


def cylinder(radius, height):
    side = 2 * math.pi * radius * height
    full = side + 2 * math.pi * radius ** 2
    return side, full


user_radius = float(input('Введите радиус: '))
user_height = float(input('Введите высоту: '))
full_square, side_area = cylinder(user_radius, user_height)
print(f'Полная площадь цилиндра: {round(full_square, 2)}\nПлощадь боковой поверхности: {round(side_area, 2)}')
