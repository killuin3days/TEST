import json
#序列化的两种方式
#1）dumps()
# file = open('domo/test.txt','w')
# name_list = ['zhangsan','lisi']
# names = json.dumps(name_list)
# file.write(names)
#2)dump()
# file = open('domo/test.txt','w')
# name_list = ['zhangsan','lisi','wuqian']
# json.dump(name_list,file)
#反序列化
#1)loads
file = open('domo/test.txt','r')
# content = file.read()
# r = json.loads(content)
# print(r)
#2)load
content = json.load(file)
print(content)

file.close()