"""
    created by 邱晨 on 2019/5/25 10:42 PM.
"""
import json

from flask import Flask,make_response
from helper import *
from yushu_book import YuShuBook

__author__ = '邱晨'

app = Flask(__name__)
app.config.from_object('config')


# 视图函数
@app.route('/hello')
def hello():
    # 基于类的视图，即插视图
    heads = {
        'content-type' : 'text/plain',
        'location' : 'http://www.baidu.com'
    }
    response = make_response('<html>hello, world!</html>', 301)
    response.headers = heads
    return response


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return json.dumps(result)


# 路由最原始写法，一般是用路由装饰器完成，极少用到这种.
# app.add_url_rule('/hello', view_func=hello)
if __name__ == '__main__':
    # 将app.run放在main下，可以保证被别的程序加载该模块的时候，不会执行
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'])
