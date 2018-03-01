# g = (x * x for x in range(10))
# print(g)

# for i in g:
#     print(i)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# fib(6)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

for i in fib(6):
    print(i)

def triangles():
    N = [1]
    while True:
        yield N
        N = [1] + [N[i] + N[i+1] for i in range(len(N)-1)] +[1]

n = 0
for t in triangles():
    print(t)
    n=n+1
    if n == 10:
        break