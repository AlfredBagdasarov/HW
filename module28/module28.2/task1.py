class Robot:
    """
    Родительский класс
    """
    def __init__(self, model, *args, **kwargs):
        self.__model = model

    def __str__(self):
        return '\n{} модель: {}'.format(self.__class__.__name__, self.__model)

    def operate(self):
        print('\nЯ - Робот!')


class CanFly:
    """
    Класс "Может летать", устанавливает высоту и скорость робота

    altitude - высота в метрах
    velocity - скорость в км/ч
    """
    def __init__(self, *args, **kwargs):
        self.altitude = 0
        self.velocity = 0

    def take_off(self):
        """ Взлет робота"""
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        """ Робот летает """
        self.altitude = 5000

    def land_on(self):
        """ Робот приземлился """
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        print('Летим')

    def __str__(self):
        return '\n{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class ScoutDrone(CanFly, Robot):
    def __init__(self, model):
        super().__init__(model)

    def operate(self):
        self.velocity += 10
        print('\nВеду разведку с воздуха')


class WarRobot(CanFly, Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('\nРобот охраняет военный объект при помощи {}'.format(self.gun))


submarine = ScoutDrone('RDR2')
print(submarine)
submarine.operate()
war = WarRobot('PDP3', 'Laser')
print(war)
war.operate()
