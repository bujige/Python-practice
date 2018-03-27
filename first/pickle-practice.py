import pickle
import json


d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

f = open('/Users/doc88/Desktop/test.txt','wb')

pickle.dump(d, f)

f.close()


f1 = open('/Users/doc88/Desktop/test.txt', 'rb')
d = pickle.load(f1)
f1.close()
print(d)


print(json.dumps(d))


obj = dict(name='小明', age=20)
s1 = json.dumps(obj, ensure_ascii=False)
s2 = json.dumps(obj, ensure_ascii=True)
print(s1)  # {"name": "小明", "age": 20}
print(s2)  # {"name": "\u5c0f\u660e", "age": 20}