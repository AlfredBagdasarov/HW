import time
from typing import Callable, Any


def timer(func: Callable) -> Any:
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.

    """
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = round(end - start, 4)
        print('Время выполнения функции: {} секунд(ы)'.format(run_time))
        return result
    return wrapped_func


@timer
def hard_func():
    return [x ** 2 ** x for x in range(21)]


hard_func()
