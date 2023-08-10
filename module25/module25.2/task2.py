class Human:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def __str__(self):
        return 'Имя: {}\t Возраст: {}'.format(self.__name, self.__age)

    def get_count(self):
        return self.__count

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            raise ValueError('Имя должно состоять только из букв.')

    def set_age(self, age):
        if age in range(0, 101):
            self.__age = age
        else:
            raise ValueError('Недопустимый возраст!')


alfred = Human('Alfred', 35)
print(alfred.get_age())
alfred._Human__age = 40
print(alfred.get_age())
