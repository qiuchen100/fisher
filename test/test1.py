# -*- coding: UTF-8 -*-


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print(exc_type)
        print(exc_value)
        print('close resource')
        b = 2
        return True

    def query(self):
        1/0
        print('query data')


with MyResource() as resource:
    resource.query()
