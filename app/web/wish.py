# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2020/1/20 7:45 AM.
"""

from flask import request, render_template, current_app, flash, redirect, url_for
from flask_login import login_required, current_user
from . import web
from app.models.wish import Wish
from app.models.base import db

__author__ = '邱晨'


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务
        # rollback
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
        flash('这本书已经成功添加到你的心愿清单！')
    else:
        flash('这本书已经添加到你的赠送清单或者心愿清单，请不要重复添加！')
    return redirect(url_for('web.book_detail', isbn=isbn))
