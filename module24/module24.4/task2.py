class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def check_info(self):
        print('Координаты в точке {}: x={}, y={}'.format(self.count, self.x, self.y))


step = Point()
step.check_info()
