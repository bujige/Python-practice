class Student(object):
    __slots__ = ('name','age')

class XiaoMing(Student):
    __slots__ = ('gender')

s = Student()

s.age = 10

x = XiaoMing()

x.age = 10