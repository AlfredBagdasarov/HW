from typing import Callable, Dict

plugins: Dict[str, Callable] = dict()


def go_to_plugins(func: Callable) -> Callable:
    plugins[func.__name__] = func
    return func


@go_to_plugins
def say_hello(name: str) -> str:
    return "Hello {name}!".format(name=name)


@go_to_plugins
def say_goodbye(name: str) -> str:
    return "Goodbye {name}!".format(name=name)


print(plugins)
print(say_hello('Tom'))
