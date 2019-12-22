"""
    created by 邱晨 on 2019/12/23 12:21 上午.
"""

from werkzeug.local import LocalStack
import threading
import time

my_obj = LocalStack()
my_obj.push(1)
# 主线程
print('before main thread %d' % my_obj.top)


def worker():
    # 新线程
    print('before new thread %s' % str(my_obj.top))
    my_obj.push(2)
    print('after new thread %d' % my_obj.top)


new_t = threading.Thread(target=worker, name='qiuchen-thread')
new_t.start()
time.sleep(1)
# 主线程
print('after main thread %d' % my_obj.top)
