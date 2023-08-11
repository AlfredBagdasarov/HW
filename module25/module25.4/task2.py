class CanFly:
    def __init__(self, height=0, speed=0):
        self.height = height
        self.speed = speed

    def fly_up(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return '\n{}: \nВысота: {}\nСкорость: {}'.format(
            self.__class__.__name__, self.height, self.speed)


class Butterfly(CanFly):
    def fly_up(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):
    def fly_up(self):
        self.height = 500
        self.speed = 1000

    def land_on(self):
        self.height = 0
        self.explosion()

    def explosion(self):
        print('Когда ракеты взлетят, какая разница, куда они упадут? (c) Том Лерер')


rock = Rocket()
rock.fly_up()
print(rock)
rock.land_on()
butterfly = Butterfly()
butterfly.fly_up()
print(butterfly)
butterfly.land_on()
print(butterfly)
