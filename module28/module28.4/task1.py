from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Абстрактный базовый класс Транспорт

    Args and attrs:
        color (str): цвет транспорта
        speed (int): скорость транспорта
    """

    def __init__(self, color: str, speed: int) -> None:
        self.color = color
        self.speed = speed

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass


class PlayMusicMixin:
    """ Класс-примесь: Проигрывает музыку """
    def play_music(self):
        print("""
        I see trees of green
        Red roses too
        I see them bloom
        For me and for you
        And I think to myself
        What a wonderful world
        """)


class Car(Transport):
    def ride_on_earth(self):
        print('Едем по земле!')


class Boat(Transport):
    def ride_on_water(self):
        print('Ходим по воде')


class Amphibian(Car, Boat, PlayMusicMixin):
    pass


amph_transport = Amphibian('green', 15)
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()
