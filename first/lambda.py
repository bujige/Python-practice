def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n:n%2==1, range(1, 20)))

print(L)


# def str(s):
#     print("global str()")
#
#
# def foo():
#     def str(s):
#         print("closure str()")
#     str("dummy")
#
#
# def bar():
#     str("dummy")
#
#
# foo()
# bar()

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')



now()

print(now.__name__)