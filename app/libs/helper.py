# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2019/5/26 4:33 PM.
"""
__author__ = '邱晨'


def is_isbn_or_key(word):
    """
    isbn isbn13 13个0-9的数字组成
    isbn10 10个0-9数字组成，含有一些'-'
    :param word: 搜索关键字
    :return: isbn or key
    :type word: str
    :rtype: str
    """
    isbn_or_key = 'key'
    short_word = word.replace('-', '')
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    elif '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
