
try:
    score = int(input("输入分数："))
    if score <= 100:
        if score >= 90:
            print("优秀")
        elif score >= 80:
            print('良好')
        elif score >= 70:
            print('中等')
        elif score >= 60:
            print('合格')
        else:
            print('不合格')
    else:
        print('输入正确分数')
except:
    print('输入正确的分数格式')
