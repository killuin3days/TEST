# def sum():
#     a = 1
#     b = 2
#     c = a+b
#     print(c)
# sum()
def sum(a,b):
    c = a+b
    return c
num1 = input("输入计算的值1:")
num2 = input("输入计算的值2:")
if type(num1)and type(num2) == int:
    int_all = int(sum(num1, num2))
    print(int_all)
elif type(num1)and type(num2) == float:
    float_num = float(sum(num1,num2))



