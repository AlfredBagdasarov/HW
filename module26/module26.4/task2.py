import random


class RandomSum:
    def __init__(self, count):
        self.last = 0
        self.end = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        self.last += random.random()
        return self.last


test = RandomSum(5)
for i in test:
    print(round(i, 2))
