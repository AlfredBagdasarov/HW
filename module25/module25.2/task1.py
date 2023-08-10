class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.count += 1

    def __str__(self):
        return 'Координаты в точке {}: x={}, y={}'.format(self.count, self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def check_value(self, value):
        if isinstance(value, (float, int)):
            return value
        return None

    def set_x(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__x = value
        else:
            raise ValueError('Введите число')

    def set_y(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__y = value
        else:
            raise ValueError('Введите число')


step = Point()
step.set_x(5)
step.set_y(5)
print(step)
