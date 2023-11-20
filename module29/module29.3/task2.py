import time
import functools
from typing import Optional, Callable, Any


def slow_it_now(_func: Optional[Callable] = None, *, count=1) -> Callable:
    """
    Декоратор, замедляющий работу функции.
    """
    def slow_down(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            start = time.time()
            print('Замедляю время выполнения функции на {} секунд(ы)'.format(count))
            time.sleep(count)
            result = func(*args, **kwargs)
            end = time.time()
            run_time = round(end - start, 4)
            print('Время выполнения функции: {} секунд(ы)'.format(run_time))
            return result

        return wrapped_func

    if _func is None:
        return slow_down
    else:
        return slow_down(_func)


@slow_it_now
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов
    для каждого N от 0 до 10000
    где 0 <= N <= 100

    :return: сумма квадратов
    """
    number = 100
    res = 0
    for _ in range(number):
        res += sum([i_num ** 2 for i_num in range(10000)])
    return res


squares_sum()
