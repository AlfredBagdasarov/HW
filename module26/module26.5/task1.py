def counter():
    num = 0
    while True:
        num += 1
        yield num


def get_prime_numbers(num):
    prime_numbers = []
    for number in range(2, num + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for i in get_prime_numbers(100000):
    print(i, end='\n')
