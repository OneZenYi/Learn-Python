'''
函数的定义和调用
'''

'''
定义函数格式
def 函数名(参数):
'''


def testDef():
    """
    这里是添加函数的注释!
    :return:
    """
    i = 0
    while i < 3:
        print("打印3遍哦!")
        i += 1


# 调用函数
testDef()

# 查看函数的注释  函数名,注意不需要加()
help(testDef)

'''
函数的参数
'''


def Name_Test(i, j):
    s = i * j
    print(s)


# 调用函数是,给参数赋值
if __name__ == '__main__':
    i = 22
    j = 40
    Name_Test(i, j)
