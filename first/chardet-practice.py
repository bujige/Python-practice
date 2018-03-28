# -*- coding: utf-8 -*-
import chardet

print(chardet.detect(b'Hello, world!'))

data ='天王盖地虎'.encode('utf-8')
print(chardet.detect(data))


data='天王盖地虎'.encode('gbk')
print(chardet.detect(data))


data='天王盖地虎'.encode('gb2312')
print(chardet.detect(data))
