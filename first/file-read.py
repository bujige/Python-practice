f = open('/Users/doc88/Desktop/test.txt', 'w')
f.write('Hello, world!')
f.close()

d = open('/Users/doc88/Desktop/test.txt', 'rb')

# print(d.read())

import os

# print(os.path.split('/Users/doc88/Desktop/testdir'))

# os.path.join('/Users/doc88/Desktop', 'testdir')

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


# file_name(os.path.abspath('.'))


# class findFile(object):
#     relativePath=''
#     def __init__(self,fileName):
#         self.fileName = fileName
#
#     def showPath(self,path = '.'):
#         self.relativePath = self.relativePath+path+'/'
#         dirs = os.listdir(self.relativePath)
#         for dir in dirs:
#             if os.path.isdir(self.relativePath+dir):
#                 if  dir != '__pycache__':
#                     self.showPath(dir)
#             else:
#                 if dir.find(self.fileName) >= 0:
#                     print(self.relativePath+dir)
#         self.relativePath=''






# from datetime import datetime
#
# pwd = os.path.abspath('.')
#
# print('      Size     Last Modified  Name')
# print('------------------------------------------------------------')
#
# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
#     print('%10d  %s  %s%s' % (fsize, mtime, f, flag))





