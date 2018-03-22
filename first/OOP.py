import types
class Student(object):

    age = 10
    def __init__(self, name, score):
        self.name = name
        self.__gender = score

    def print_score(self):
        print('%s %s' % (self.name,self.score))

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')

# li = Student('li',55)
#
# a = Student('A',23)
# b = Student('B',27)

# print(a.name,a.print_score(),a.name)
# print(b.name,b.print_score())

# li.print_score()

# bart = Student('Bart Simpson', 59)
# print(bart.get_name())
#
# bart.__name = 'New Name' # 设置__name变量！
# print(bart.__name)
# print(bart.get_name())

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

print(type(abs) == types.BuiltinFunctionType)

print(isinstance(bart,Student))

# print(dir(Student))

def prn_obj(obj):
  print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

# prn_obj(Student)

print(vars(bart))

print(Student.age)

bart.age = 15

print(bart.age)

print(Student.age)