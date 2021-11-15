def demo_01():
    print('1.无参数,无返回值')


demo_01()


def demo_02():
    tem = 28
    print('2.无参数,有返回值')
    return tem


tem = demo_02()
print(tem)


def demo_03(num):
    num += 28
    print('3.有参数,无返回值')


demo_03(100)


def demo_03(num):
    num += 28
    print('3.有参数,有返回值')
    return num


tem = demo_03(100)
print(tem)


def func():
    """
    当前函数返回多个数据
    :return:
    """
    tem = 27
    wetness = 98
    pm_25 = 76
    # list_1 = [tem, wetness, pm_25]  # 多函数,用列表\元组\字典
    # 元组可以拆分
    return tem, wetness, pm_25


a, b, c = func()
print(a)
print(b)
print(c)
