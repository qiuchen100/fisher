"""
    created by 邱晨 on 2019/12/23 12:21 上午.
"""
import threading
import time
from werkzeug import Local


class A:
    b = 1


my_obj = Local()
my_obj.b = 1


def worker():
    # 新线程
    my_obj.b = 2
    print('new thread %d' % my_obj.b)


new_t = threading.Thread(target=worker, name='qiuchen-thread')
new_t.start()
time.sleep(1)
# 主线程
print('main thread %d' % my_obj.b)
