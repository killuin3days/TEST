f = open("domo/test.txt", 'r')#a为像文件中追加，w是覆盖数据，r是读取数据
# f.write('sha1bi\n'*5)
# rf = open('domo/test.txt','r')
content = f.readline() #readlines 会返回列表 readline会读写第一列
print(content)
f.close()