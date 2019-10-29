# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2019/5/25 10:42 PM.
"""

from app import create_app

__author__ = '邱晨'

app = create_app()


if __name__ == '__main__':
    # 将app.run放在main下，可以保证被别的程序加载该模块的时候，不会执行
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'])
