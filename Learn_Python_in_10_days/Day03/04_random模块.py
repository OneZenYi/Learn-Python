import random

# 随机数

# 随机 0到100的整数
print(random.randint(0, 100))

'''
石头剪刀布 游戏设计
'''
# 玩家数据
a = int(input("请输入:"))

# 电脑数据
b = random.randint(1, 3)
print(b)

# 石头(1) 剪刀(2) 布(3)
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("用户赢了!")
    print('用户出的是:'+str(a),',电脑出的是:'+str(b))
elif a == b:
    print("我们是平手")
    print('用户出的是:'+str(a),',电脑出的是:'+str(b))
else:
    print('电脑赢了!')
