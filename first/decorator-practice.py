# -*- coding:utf-8 -*-
import functools
import time


# def metric(fn):
#     def wrapper(args, **kw):
#         fstart = time.time()
#         f = fn(args,**kw)
#         fend = time.time()
#         print('%s executed in %s ms' % (fn.__name__, fend-fstart))
#         return f
#     return wrapper

def metric(fn):
    @functools.wraps(fn)
    def warpper(*args, **kw):
        fstart = time.time()
        k = fn(*args, **kw)
        fend = time.time()
        print('%s executed in %s ms' % (fn.__name__, fend-fstart))
        return k
    return warpper


def log(text=''):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s %s():' % (text, func.__name__))
            fn = func(*args, **kw)
            print('end call %s %s():' % (text, func.__name__))
            return fn
        return wrapper
    return deco


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

@log() #要有括号
def now1():
    print('2011-01-02')

@log('exe')
def now2():
    print('2011-01-02')

now1()
now2()