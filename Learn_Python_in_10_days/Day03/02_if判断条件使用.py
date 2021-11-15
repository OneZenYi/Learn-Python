'''
if 语句判断
'''

# x = int(input("你今年多少岁:"))
# if x >= 18:
#     print('您已满%s岁,请进入网吧!' % x)
# elif x >= 15:
#     print('你已满%s岁,请回家打王者!' % x)
# else:
#     print('您未满%s岁,请离开网吧!' % x)

'''
if 与逻辑运算符 and  or  not
'''
# a = int(input("你今年多少岁:"))
#
# if a > 0 and a >= 120:
#     print('你的年龄是%s' % a)
# elif a >= 20 and a <= 35:
#     print('你的年龄是%s,正如年轻力壮!' % a)
# else:
#     print('%s岁不属于青年范围!' % a)

'''
if 的嵌套
'''
a = input("请输入是否购买火车票!(是/否):")
if a=='是':
    x=input("请输入是否带刀!(是/否):")
    if x=='是':
        d = int(input("刀是否超过20cm,请填写长度!:"))
        if d<=20:
            print('你的刀大于%s,属于违禁品!'%d)
        else:
            print('进入安保室,进行检查!')
    else:
        print('请进入等候区上车!')
else:
    print('请先购买火车票!')