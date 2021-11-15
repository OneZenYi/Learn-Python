'''
数据类型转换
'''

# int(x) 将数据转换为整数
a = 123.6
print(int(a))
print(type(int(a)))

# float(x)
print(float(a))

# str(x)
print(str(a))

# list(x)  只有有序的才能转换成列表 字典不能转换成列表
x = 'hello'  # (1,2,2,3)  [1,2,3,4,6]
x1 = (1, 2, 2, 3)
print(list(x))
print("".join(list(x)))  # 用 join 拼接数据 (字符串\列表\元组)

# tuple(x)
s = 'hello'  # [1,2,3,4,6]
print(tuple(s))
