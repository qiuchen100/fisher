# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2020/1/20 7:45 AM.
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError
from app.models.user import User
__author__ = '邱晨'


class LoginForm(Form):
    email = StringField(
        validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范！')])

    password = PasswordField(
        validators=[DataRequired(message='密码不可以为空，请输入密码！'), Length(6, 32)])


class RigisterForm(LoginForm):
    nickname = StringField(
        validators=[DataRequired(), Length(2, 10, message='昵称需要2至10个字符！')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已经被注册！')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经存在！')
