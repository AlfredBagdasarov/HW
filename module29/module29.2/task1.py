import time
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(time.time() - start)


with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 1000000
    val_1 += 'abc'

with timer() as t2:
    print('Вторая часть')
    val_2 = 200 * 200 ** 1000000

with timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 1000000
