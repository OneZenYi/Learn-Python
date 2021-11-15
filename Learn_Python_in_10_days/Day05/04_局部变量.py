'''
局部变量
'''


def demo_001():
    # 定义局部变量
    num = 100
    print(num)
    return num


def demo_002():
    num= demo_001()

    print(num+1)


demo_002()