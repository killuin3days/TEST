'''
a = 36
a > 10 and print('hello world')
#and的性能优化，当and前面的结果是false的情况下，后边代码不执行
a < 10 and print('hello world')
'''
b = 32
b > 34 or print('hello world')
#or的性能优化，只要有一边是Ture那么返回
b > 1 or print('hello world')