from functools import reduce

def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])

# print(list(r))


def add(x,y):
    return x + y

# print(reduce(add,[1,2,3,4,5,6,7,8,9,10]))

def fn(x,y):
    return x*10 + y

def charToNum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(charToNum,'123456')))

def strToInt(s):
    def fn(x,y):
        return x*10+y
    def charToNum(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    return reduce(fn,map(charToNum,s))

print(strToInt('323423'))