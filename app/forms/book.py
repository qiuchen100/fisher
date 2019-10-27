"""
    created by 邱晨 on 2019/5/26 12:12 AM.
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange

__author__ = '邱晨'


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)