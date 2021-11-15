"""
__str__ 方法
"""


class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃鱼儿" % self.name)

    def __str__(self):
        print("自动调用")
        return "名字是:%s " % self.name


big_cat = Cat("大脸猫")
print(big_cat)
