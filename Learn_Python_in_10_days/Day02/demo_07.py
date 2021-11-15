'''
字符串拆分
'''

my_str = 'hello ,world!,Python,world!'
# 切分 split(num='次数'),返回是列表数据
print(my_str.split(','))
# 字段次数来切分
print(my_str.split(',', 1))

# 不算数据切分数据,系统会安装转义字符与空格来切分
my_str_ = 'hol\rle ,worl\nd!,Pyt\thon,wo rld!'
print(my_str_.split())

# 切分 splitlines 按行来切分,返回是列表数据
print(my_str_.splitlines())

# 字符串拼接 join()  用 + 拼接
mys = 'hello'
mya = 'python'
print('#'.join(mya))
print(mya + mys)
