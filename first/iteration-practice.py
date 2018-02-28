def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    Max = Min = L[0]
    for i in L:
        if i > Max:
            Max = i
        elif i < Min:
            Min = i
    return (Min, Max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')