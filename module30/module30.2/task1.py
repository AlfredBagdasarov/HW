import functools
from typing import Callable, Any

global_count = {}


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий
    количество вызовов декорируемой функции.
    """
    local_count = {}

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        global global_count
        nonlocal local_count
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        local_count[func.__name__] = local_count.get(func.__name__, 0) + 1
        print(global_count, local_count)
        return func(*args, **kwargs)

    wrapped_func.check_count = local_count
    return wrapped_func


@counter
def hello():
    print('hello')


@counter
def hello_2():
    print('hello')


hello()
hello()
hello_2()
hello_2()
print(hello_2.check_count)

print('Результат выполнения работы команды:')
print(dir(__builtins__))
