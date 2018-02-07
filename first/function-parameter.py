def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def calc_sum(*number):
    sum = 0
    for i in number:
        sum += i*i
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# print power(5)
# print power(5,3)

# print calc_sum(*[1,2,3])

person('ysc',18)
person('XiaoMing', 22, job='developer')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)