import random


class Toyota:
    color = 'yellow'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def info(self):
        print('Цвет авто: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}'.format(
            self.color, self.price, self.max_speed, self.current_speed
        ))

    def change_speed(self, new_speed):
        self.current_speed = new_speed


car = Toyota()
car.info()
car.change_speed(random.randint(0, 200))
car.info()
