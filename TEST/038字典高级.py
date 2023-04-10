person = {'name':'wuqian','age':'28'}
# print(person['name'])
# print(person.get('sex'))

# person['name'] = 'zhangsan' #字典修改
# print(person)
person['sex'] = '南' #若该键不存在会添加，若存在则会修改
print(person)

#删除del用法，删除某个元素
# del person['name']
# print(person)
#删除clear用法,清空字典
# person.clear()
# print(person)
#遍历字典
#1)遍历字典的key
for key in person.keys():
    print(key)
#2)遍历字典的value
for value in person.values():
    print(value)
#3)遍历字典的key,value
for key,value in person.items():
    print(key,value)
#4)遍历字典的项/元素
for item in person.items():
    print(item)