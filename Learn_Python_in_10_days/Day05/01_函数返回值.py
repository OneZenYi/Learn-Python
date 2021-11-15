'''
函数返回值
'''


def Name_Test(i, j):
    sum = i * j
    print(sum)

    # 返回结果值,提前终止函数运行
    return sum


# 调用函数是,给参数赋值
if __name__ == '__main__':
    i = 22
    j = 40
    res = Name_Test(i, j)
    print(res)

