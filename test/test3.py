# -*- coding: UTF-8 -*-

import threading
import time


def worker():
    time.sleep(2)
    print('i am thread')
    t = threading.currentThread()
    print(t.getName())

# 更加充分的利用CPU的性能优势
# 异步编程的另一种方式


new_t = threading.Thread(target=worker, name='qiuchen-thread')
new_t.start()
t = threading.currentThread()
print(t.getName())
# 主线程
