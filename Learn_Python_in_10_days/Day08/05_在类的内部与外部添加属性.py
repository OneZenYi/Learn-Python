"""
添加外部属性
"""


# 在类的外部添加属性
# 对象名.属性名=属性值
class Cat:

    def eat(self):
        # 通过 self 参数,访问属性  self.属性名

        # 在类的内部 访问属性 对象名.属性名
        # 在类的内部 调用方法 对象名.方法名(参数)
        print("%s爱吃鱼!" % self.name)

    def drink(self, water):
        print("我爱喝水!:%s" % water)


tom = Cat()
# 对象名.属性名=属性值
tom.name = "汤姆猫"
# 在类的外部访问属性
print(tom.name)
# 对象名.方法名()
tom.eat()

tom1 = Cat()
# 对象名.属性名=属性值
tom1.name = "大懒猫"
# 在类的外部访问属性
print(tom1.name)
# 对象名.方法名()
tom1.eat()

"""
添加内部属性
"""


# 在类的内部添加属性
class Cat_a:

    def eat(self):
        # 通过 self 参数,访问属性  self.属性名
        print("%s爱吃鱼!" % self.name)

        # 在类的内部 访问属性 self.属性名
        # 在类的内部 调用方法 self.方法名(参数)
        self.drink("哈哈哈")
        self.drink("嘻嘻嘻")

    def drink(self, water):
        print("%s爱喝水!" % water)


tom = Cat_a()
# 对象名.属性名=属性值
tom.name = "汤姆猫"
# 在类的外部访问属性
print(tom.name)
# 对象名.方法名()
tom.eat()
