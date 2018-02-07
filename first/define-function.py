import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    x1 = (-b+math.sqrt(abs(b*b-4*a*c)))/(2*a)
    x2 = (-b-math.sqrt(abs(b*b-4*a*c)))/(2*a)
    return x1, x2


print(my_abs(-9))

x,y = move(100, 100, 60, math.pi / 6)
print(x,y)

x1,x2 = quadratic(1,2,1)
print x1,x2