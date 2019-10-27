"""
    created by 邱晨 on 2019/5/26 12:12 AM.
"""
__author__ = '邱晨'

DEBUG = True
PORT = 81

DB_HOST = 'db.360haojie.loan'
DB_PORT = 3306
DB_NAME = 'dmg'
USER_NAME = 'dmg'
USER_PWD = 'dmg123456!'

SQLALCHEMY_DATABASE_URI = f'mysql+cymysql://{USER_NAME}:{USER_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'