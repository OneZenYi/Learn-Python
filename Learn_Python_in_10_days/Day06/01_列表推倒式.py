# range 函数 产生序列数的对象
# range 语法(起始位置,结算位置,步长)
import random

x = range(10, 0, -2)

for i in x:
    print(i)

"""
列表推倒式
语法:[包含变量表达式 for 变量 in range(范围值)]
"""
print([x for x in range(10)])
print("_" * 50)

print([i for i in range(0, 10, 2)])
print("_" * 50)

print([i + 100 for i in range(0, 10, 2)])
print("_" * 50)

print([i * i for i in range(10)])
print("_" * 50)

# 不使用步长,需要用到判断. if i % 2 == 0
print([i for i in range(21) if i % 2 == 0])
print("_" * 50)

# 随机100次, 100以内的随机数
list_1 = ([random.randint(0, 100) for i in range(100)])
print(list_1)
print("_" * 50)
# 使用推到数遍历列表里面的数据+100
print([i + 100 for i in list_1])
print("_" * 50)
# 遍历里面的数是偶数
print([i + 100 for i in list_1 if i % 2 == 0])
