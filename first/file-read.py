f = open('/Users/doc88/Desktop/test.txt', 'w')
f.write('Hello, world!')
f.close()

d = open('/Users/doc88/Desktop/test.txt', 'rb')

print(d.read())

import os

print(os.path.abspath('.'))

# os.path.join('/Users/doc88/Desktop', 'testdir')

os.rmdir('/Users/doc88/Desktop/testdir')

