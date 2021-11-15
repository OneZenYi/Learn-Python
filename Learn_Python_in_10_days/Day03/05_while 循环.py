"""
while 循环
"""

# 循环初始
'''
初始条件设置
while 条件(判断 计数器 是否达到 目标次数):
    条件满足是,做的事情
    条件满足是,做的事情
    处理条件(计数器+1)
'''

# 循环5遍我爱你
a = 1
while a <= 5:
    print('我爱你,我爱你!', a)
    a += 1

print('-' * 50)
'''
Python 中计数法则
'''
b = 0
while b < 5:
    print('我爱你,我爱你!', b)
    b += 1

print('-' * 50)
# 倒序
c = 10
while c > 0:
    print("我不爱你!", c)
    c -= 1

print('_' * 50)
'''
用 while 循环计算 1-100 的和
'''
i = 0
sum = 0
while i < 100:
    i += 1
    sum = sum + i
    print('1-100数相加总和:%s' % sum)

print("-" * 50)
'''
用 while 循环计算 1-100 的和 取偶数
'''
i = 0
sum = 0
while i < 100:
    i += 1
    # sum = sum + i
    if i % 2 == 0:   # 打印所有的偶数, if i % 2 != 0 打印所有的奇数
        sum = sum + i
        print('1-100数相加总和:%s' % sum)

