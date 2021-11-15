"""
Print() 函数使用
"""
print("你好,Holle World!")
print(13142077777)
print("I'm,is onezen")

"""
多行注释  """ """  或 ''' '''
单号注释  #  ctrl+/
"""
print("I'm,is onezen")
'''
变量定义
'''
mun = "123"
str = "O(∩_∩)O哈哈~" + mun

print(str)

'''
买苹果案例: 苹果8.5/斤,买7斤,满50减5元
'''
print("买苹果案例: 苹果8.5/斤,买7斤,满50减5元")
univalent = 8.5
weight = 7
discount = 5

money = univalent * weight - discount
print("需要支付:", money)

# 动态变量买苹果程序
# univalent_ = float(input(print("请输入苹果单价:")))
# weight_ = float(input(print("请输入苹果重量:")))
#
# money_ =univalent_ * weight_
# print('购买苹果总金额:',money_)
# if money_ >= 50:
#     print('金额满50元优惠5元')
#     print("您需要支付:", money_ - 5)
# else:
#     print("您需要支付:", money_)

'''
查看 Python关键字
'''
import keyword

print(keyword.kwlist)

'''
占位符 %s(字符串)  %d(数字) %f(浮点数)  %%(表示一个%),占位符都可以替换成%s
'''

name = '小姨妈'
age = 26
gender = '女'
high = 17.86
print('我叫 %s,性别%d,今年%s岁,身高%0.2f' % (name, age, gender, high))
