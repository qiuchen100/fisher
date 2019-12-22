"""
    created by 邱晨 on 2019/8/31 7:45 PM.
"""

from flask import jsonify, request
from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel

__author__ = '邱晨'


@web.route('/test')
def test():
    from app.libs.non_local import n
    print(n.v)
    n.v = 2
    print(n.v)
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print(request.v)
    return ''


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字 isbn
    :param page: start count
    :return:
    """
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        # return json.dumps(result), 200, {'content-type':'application/json'}
        return jsonify(result)
    return jsonify(form.errors)

# 路由最原始写法，一般是用路由装饰器完成，极少用到这种.
# app.add_url_rule('/hello', view_func=hello)
