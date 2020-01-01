# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2020/1/20 7:45 AM.
"""

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user
from . import web
from app.forms.auth import RigisterForm, LoginForm
from app.models.user import User
from app.models.base import db

__author__ = '邱晨'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RigisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next_url = request.args.get('next')
            if not next_url or not next_url.startswith('/'):
                next_url = url_for('web.index')
            return redirect(next_url)
        else:
            flash('账号不存在或密码错误！')
        pass
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


# @web.route('/reset/password/<token>', methods=['GET', 'POST'])
# def forget_password_request(token):
#     pass
