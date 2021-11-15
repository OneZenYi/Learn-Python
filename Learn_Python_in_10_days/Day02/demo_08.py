'''
字符串 切片
'''

name = 'zhangyi,hello'
# 字符串[开始位置:结算位置:步长]
print(name[0:13])
print(len(name))# 字符长度
print(name[8:13])
print(name[8:])

print(name[-1:-10:-1])# 倒序切片,步长必须是复数
print(name[13::-1])



