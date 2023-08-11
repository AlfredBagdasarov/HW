class Unit:
    def __init__(self, hp):
        self.__hp = hp

    def __str__(self):
        return '\nУ {} Осталось очков здоровья: {}'.format(
            self.__class__.__name__, self.__hp)

    def set_hp(self, amount):
        self.__hp = amount

    def get_hp(self):
        return self.__hp

    def get_damage(self, amount):
        self.set_hp(self.get_hp())


class Soldier(Unit):
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount)


class Citizen(Unit):
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount * 2)


soldier = Soldier(100)
soldier.get_damage(5)
print(soldier)
citizen = Citizen(100)
citizen.get_damage(5)
print(citizen)
