"""
多值参数
"""


# *args 接收多余的参数
# **kwargs 接收多余的关键字参数
def demo(num, *args, **kwargs):
    print(num, args, kwargs)


demo(10, 2, 3, 4, 5, name="1231", age=23)

print("*" * 50)


# 将参数值累加
def demo01(*args):
    sum = 0
    for i in args:
        sum += i

    return sum


r = demo01(123, 123)
print(r)
r = demo01(123, 123, 12322, 22)
print(r)
print("*" * 50)

"""
多值参数,组包与拆包
"""


def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


print("*" * 50)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    print("*" * 50)

    # 组包参数
    test(a, b, args, kwargs)
    print("*" * 50)

    # 拆包元组参数
    test(a, b, *args, kwargs)
    print("*" * 50)

    # 拆包元组,字典参数
    test(a, b, *args, **kwargs)


test1(10, 20, 30, 40, 50, name="小米", age=20)
