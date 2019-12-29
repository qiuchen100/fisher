# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2019/8/31 7:45 PM.
"""

from flask import jsonify, request, render_template, flash
import json
from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection

__author__ = '邱晨'


@web.route('/test')
def test():
    r = {
        'name': '七月',
        'age': 18
    }
    flash('hello, qiuchen', category='notice')
    flash('hello, Bob', category='notice')
    flash('xxxxxxxxxx', category='warning')
    return render_template('test4.html', data=r)


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books.__dict__)
    else:
        return jsonify(form.errors)

# 路由最原始写法，一般是用路由装饰器完成，极少用到这种.
# app.add_url_rule('/hello', view_func=hello)
