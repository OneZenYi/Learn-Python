"""
多层继承
"""


# 定义爷爷类
class Animal:
    """动物类,父类"""

    def __init__(self):
        self.name = "动物"
        self.age = 2

    def eat(self):
        print("%s 都爱吃东西" % self.name)


# 定义父亲类
class Cat(Animal):
    """猫类,单继承,动物类"""

    def catch(self):
        print("猫抓老鼠")


# 定义孙子类
class BoSiMao(Cat):
    """单继承,猫类"""

    def sing(self):
        print("波斯猫在唱歌")

if __name__ == '__main__':
    bsm = BoSiMao()
    bsm.sing()
    bsm.eat()
    bsm.catch()
