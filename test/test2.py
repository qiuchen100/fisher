# -*- coding: UTF-8 -*-


import time
from contextlib import contextmanager


class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self

    # def __exit__(self, exc_type, exc_value, tb):
    #     print(exc_type)
    #     print(exc_value)
    #     print('close resource')
    #     return True

    def query(self):
        print('query data')


# with MyResource() as resource:
#     resource.query()


@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource')
    return True


with make_myresource() as r:
    r.query()


@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')


with book_mark():
    print('且将生活饮而尽', end='')
