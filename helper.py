"""
    created by 邱晨 on 2019/5/26 4:33 PM.
"""
__author__ = '邱晨'


def is_isbn_or_key(word):
    """
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