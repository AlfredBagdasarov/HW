class Primes:
    def __init__(self, count):
        self.count = count
        self.step_num = 1
        self.prime_number = []

    def __iter__(self):
        self.step_num = 1
        return self

    def __next__(self):
        while self.step_num <= self.count:
            self.step_num += 1
            for i_prime in self.prime_number:
                if self.step_num % i_prime == 0:
                    break
            else:
                self.prime_number.append(self.step_num)
                return self.step_num
        raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')
