import os
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def in_dir(path) -> Iterator:
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cur_path)


with in_dir('C:\\'):
    print(os.listdir())
