from functools import reduce

def normalize(name):
    return name[0].upper() + name[1:].lower()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

def prod(L):
    def muti(x,y):
        return x*y
    return reduce(muti,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    s1,s2 = s.split('.')
    print(s1,s2)
    def charToNum(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    def fn(x,y):
        return x*10+y
    def fm(x,y):
        return x*10+y
    print(list(map(charToNum,s2)))
    return reduce(fn,map(charToNum,s1)) + reduce(fm,map(charToNum,s2))/(10**len(s2))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')