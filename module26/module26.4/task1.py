class CountIterator:
    counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        CountIterator.counter += 1
        return CountIterator.counter


my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)
