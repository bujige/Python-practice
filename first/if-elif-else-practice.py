# coding=UTF-8

height = 1.68
weight = 65.5

bmi = weight/(height*height)
if bmi < 18.5:
    print('bmi: = %f 过轻' % bmi)
elif 18.5 <= bmi < 25:
    print('bmi: = %f 正常' % bmi)
elif 25 <= bmi < 28:
    print('bmi: = %f 过重' % bmi)
elif 28 <= bmi < 32:
    print('bmi: = %f 肥胖' % bmi)
else:
    print('bmi: = %f 严重肥胖' % bmi)
