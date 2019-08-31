"""
    created by 邱晨 on 2019/8/31 7:45 PM.
"""

from flask import jsonify
from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = '邱晨'


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type':'application/json'}
    return jsonify(result)

# 路由最原始写法，一般是用路由装饰器完成，极少用到这种.
# app.add_url_rule('/hello', view_func=hello)

