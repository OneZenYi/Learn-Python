"""
缺省参数
"""

# 缺省参数(带有默认值的参数),必须放在必须参数的后面.
def func(name, age=20, psoition='同学'):
    print(name, age, psoition)


# 缺省参数传参
func("张狗蛋", 30, "班长")
# 不传参数,就使用默认参数
func("张狗蛋")
# 使用关键字传参
func(name="张狗蛋", psoition="班长", age=30)
# 没有默认值的参数,属于必须参数,必须传值
func("张小蛋")