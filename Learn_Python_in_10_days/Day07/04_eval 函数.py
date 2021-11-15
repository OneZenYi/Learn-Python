"""
eval 函数 是计算函数   将字符串的双引号去除   不能转换空字符串
"""


def calc():
    info = input("请输入加减乘除混合运算式:")

    print(eval(info))


calc()
