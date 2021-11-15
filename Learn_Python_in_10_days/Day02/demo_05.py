'''
字符串查找与替换
'''

my_str = 'hello,Python3'

# 判断字符串以什么开头
print(my_str.startswith('ho'))
# 判断字符串以什么结束
print(my_str.endswith('3'))

# 查找 find(字符串,start=0,end=len(字符串))
print(my_str.find('ll'))
# 没有查找到数据, 返回 -1
print(my_str.find('123'))

# 查找 index(字符串,start=0,end=len(字符串))
print(my_str.index('e'))
# 用index查找字符,找不到字符会报错
# my_str.index('123')
