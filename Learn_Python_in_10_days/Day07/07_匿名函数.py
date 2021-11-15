"""
匿名函数
"""

# 函数名就变量名,保存就是函数当前的引用地址

""" lambda 表达式
语法:lambda 参数:表达式
"""

# 不带参数
# 匿名函数
lambda: 100
# 调用函数
(lambda: 100)()
# 打印函数
print((lambda: 100)())

print("_" * 50)

# 带一个参数
# 匿名函数
func = lambda x: x + 100
# 调用函数
print((lambda x: x + 100)(100))
print(func(50))

print("_" * 50)

# 带二个参数
# 匿名函数
func = lambda x, y: x + y
# 调用函数
print((lambda x, y: x + y)(100,300))
print(func(50, 10))
