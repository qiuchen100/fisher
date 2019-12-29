"""
    created by 邱晨 on 2019/5/26 12:12 AM.
"""
# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2019/5/26 12:12 AM.
"""

__author__ = '邱晨'

DEBUG = True
PORT = 81

DB_HOST = '192.168.1.120'
DB_PORT = 3306
DB_NAME = 'fisher'
USER_NAME = 'root'
USER_PWD = '123456!'

SQLALCHEMY_DATABASE_URI = f'mysql+cymysql://{USER_NAME}:{USER_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SECRET_KEY = 'ua678Yzg677szo567'
