# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2020/1/20 7:45 AM.
"""

from flask import request, render_template, current_app, flash, redirect, url_for
from flask_login import login_required, current_user
from . import web
from app.models.gift import Gift
from app.models.base import db

__author__ = '邱晨'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务
        # rollback
        with db.auto_commit():
            gift = Gift()
            gift.uid = current_user.id
            gift.isbn = isbn
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
        flash('这本书已经成功添加到你的赠送清单！')
    else:
        flash('这本书已经添加到你的赠送清单或者心愿清单，请不要重复添加！')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
