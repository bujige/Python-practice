def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        pass
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
        pass


move(10,'a','b','c')