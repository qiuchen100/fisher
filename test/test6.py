"""
    created by 邱晨 on 2019/12/23 12:21 上午.
"""

from werkzeug.local import LocalStack

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.pop())

s.push(2)
s.push(3)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
