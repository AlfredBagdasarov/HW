class Robot:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\n{} модель: {}'.format(self.__class__.__name__, self.__model)

    def operate(self):
        print('\nРобот ездит по кругу!')


class VacuumCleanerRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        print('\nРобот пылесосит пол')
        print('\nТекущая заполненность мешка для мусора:', self.garbage_bag)


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('\nРобот охраняет военный объект при помощи {}'.format(self.gun))


class SubmarineRobot(WarRobot):
    def __init__(self, model, gun, depth):
        super().__init__(model, gun)
        self.depth = depth

    def operate(self):
        super().operate()
        print('\nОхрана ведется под водой на глубине', self.depth)


submarine = SubmarineRobot('RDR2', 'Torpedo', 15)
print(submarine)
submarine.operate()
war = WarRobot('PDP3', 'Laser')
print(war)
war.operate()
clean = VacuumCleanerRobot('HTML12')
clean.garbage_bag += 15
print(clean)
clean.operate()
