import random


class Toyota:

    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print('Цвет авто: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}\n'.format(
            self.color, self.price, self.max_speed, self.current_speed
        ))

    def change_speed(self, new_speed):
        self.current_speed = new_speed


car_1 = Toyota('yellow', 1000000, 180, 15)
car_2 = Toyota('black', 1500000, 200, 120)
car_1.change_speed(random.randint(0, 200))
car_1.info()
car_2.info()
