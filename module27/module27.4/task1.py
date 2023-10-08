from typing import Callable, Any


def bread(func: Callable) -> Callable:
    """ Декоратор, заполняющий сандвич булочкой"""
    def wrapped_bread(*args, **kwargs) -> Any:
        print('</----------\>')
        func(*args, **kwargs)
        print('<\______/>')
    return wrapped_bread


def ingredients(func: Callable) -> Callable:
    """ Декоратор, заполняющий сандвич ингридиентами """
    def wrapped_ingredients(*args, **kwargs):
        print('#помидоры#')
        func(*args, **kwargs)
        print('~салат~')

    return wrapped_ingredients


@bread
@ingredients
def filling_burger(filler: Callable) -> Any:
    print(filler)


filling_burger('ветчина')
