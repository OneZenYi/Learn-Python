"""
实例对象,实例属性,实例方法
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃美食!" % self.name)


# 创建对象在内存空间中实际存在的,叫实例对象
xm = Person("小胡")
print(xm)  # 实例对象中的属性是实例属性
print("id(xm)", id(xm))
xm.eat()  # 属于实例对象可以调用的方法,并且具有self参数,是实例方法
print("id(xm)", id(xm.eat))

print("*" * 50)

xw = Person("小王")
print(xw)  # 实例对象中的属性是实例属性
print("id(xw)", id(xw))
xm.eat()  # 属于实例对象可以调用的方法,并且具有self参数,是实例方法
print("id(xw)", id(xw.eat))
