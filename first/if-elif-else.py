# coding=UTF-8

age = 10
if age > 30:
    print('yes')
else:
    print('no')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')