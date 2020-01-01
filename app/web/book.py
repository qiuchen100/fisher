# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2019/8/31 7:45 PM.
"""

from flask import jsonify, request, render_template, flash
from flask_login import current_user
import json
from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeViewModel
from app.models.gift import Gift
from app.models.wish import Wish

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
    return render_template('test.html', data=r)


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
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books.__dict__)
    else:
        flash('搜索的关键字不符合要求，清重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)

# 路由最原始写法，一般是用路由装饰器完成，极少用到这种.
# app.add_url_rule('/hello', view_func=hello)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
    :param isbn
    :return:
    """
    has_in_gifts = False
    has_in_wishes = False
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    if current_user.is_authenticated:
        has_in_gifts = current_user.has_in_gifts(isbn)
        has_in_wishes = current_user.has_in_wishes(isbn)
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    trade_gifts_model = TradeViewModel(trade_gifts)
    trade_wishes_model = TradeViewModel(trade_wishes)
    print('has_in_gifts: {}'.format(has_in_gifts))
    print('has_in_wishes: {}'.format(has_in_wishes))
    return render_template('book_detail.html', book=book, wishes=trade_wishes_model, gifts=trade_gifts_model, has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)


@web.route('/book/my_wish')
def my_wish():
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    pass


@web.route('/book/pending')
def pending():
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    pass


@web.route('/book/send_drift/<gid>')
def send_drift(gid):
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    pass


@web.route('/book/satisfy_wish/<wid>')
def satisfy_wish(wid):
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    pass
