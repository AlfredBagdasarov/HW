import functools
from datetime import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    """ Декоратор. Выводит время запуска функции или метода """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('\nЗапуск функции "{}" произошел в:'.format(func.__name__), datetime.utcnow())
        print('Документация функции (метода):\n', func.__doc__)
        print('Args и kwargs функции:', func(*args, **kwargs))
        return func(*args, **kwargs)

    return wrapper


def decorator(cls):
    for i_method_name in dir(cls):
        if i_method_name.startswith('__') is False:
            cur_method = getattr(cls, i_method_name)  # берем метод по названию
            decorated_method = logging(cur_method)  # логируем выбранный метод
            setattr(cls, i_method_name, decorated_method)  # заменяем старый метод на новый
    return cls


@decorator
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        """
        Функция нахождения суммы квадратов
        для каждого N от 0 до 10000
        где 0 <= N <= 100

        :return: сумма квадратов чисел
        """
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_num)])

        return result

    def cubes_sum(self, number: int) -> int:
        """
        Функция нахождения суммы кубов
        для каждого N от 0 до 10000
        где 0 <= N <= 100

        :return: сумма кубов чисел
        """
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])

        return result


my_funcs_1 = Functions(max_num=1000)
my_funcs_1.squares_sum()
my_funcs_1.cubes_sum(number=2000)
