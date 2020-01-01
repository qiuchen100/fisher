"""
    created by 邱晨 on 2019/8/31 9:49 PM.
"""
from flask import Blueprint

__author__ = '邱晨'

# 蓝图 blueprint
web = Blueprint('web', __name__)

from app.web import main
from app.web import drift
from app.web import book
from app.web import auth
from app.web import gift
from app.web import wish