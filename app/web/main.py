# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2020/1/20 7:45 AM.
"""
from . import web


@web.route('/')
def index():
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    return 'index.html'
