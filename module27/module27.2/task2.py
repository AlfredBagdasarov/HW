import time
from typing import Callable, Any


def timer(func: Callable, *args, **kwargs) -> Any:
    """ Функция-таймер. Выводит время работы функции и возвращает ее результат """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    run_time = round(end - start, 4)
    print('Время выполнения функции: {} секунд(ы)'.format(run_time))
    return result


def hard_func():
    return [x ** 2 ** x for x in range(21)]


my_time = timer(hard_func)
