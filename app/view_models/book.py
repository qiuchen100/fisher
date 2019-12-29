# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2019/5/25 10:42 PM.
"""
__author__ = '邱晨'


class BookViewModel:
    def __init__(self, book):
        self.title = book['title'],
        self.publisher = book['publisher'],
        self.pages = book['pages'],
        self.author = '、'.join(book['author']),
        self.price = book['price'],
        self.summary = book['summary'],
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword
