import functools
from collections.abc import Callable


def repeat(count: int) -> Callable:
    """ Декоратор, который вызывает декорируемую функцию
        столько раз, сколько укажет пользователь.
    """
    def wrap_func(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
            return
        return wrapped_func
    return wrap_func


@repeat(15)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
