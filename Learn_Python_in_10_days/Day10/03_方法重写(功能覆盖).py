"""
方法重写(功能覆盖)
# 方法重写的前提, 必须有继承关系
"""


# 子类中有父类的相同的方法名,子类重写了父类的方法

# 定义爷爷类
class Animal:
    """动物类,父类"""

    def __init__(self):
        self.name = "动物"
        self.age = 2

    def eat(self):
        print("%s 都爱吃东西!" % self.name)


# 定义父亲类
class Cat(Animal):
    """猫类,单继承,动物类"""

    def catch(self):
        print("猫抓老鼠!")


# 定义孙子类
class BoSiMao(Cat):
    """单继承,猫类"""

    def sing(self):
        print("波斯猫在唱歌!")

    def catch(self):
        print("波斯猫喜欢抓鱼!")

    def eat(self):
        # 功能扩展:在子类调用父类的方法
        # 语法: super().重写方法名()
        # 父类名.方法(self)

        # Animal.eat(self)  # 不建议使用
        super().eat()  # 建议使用这个方法

        print("喜欢吃鱼罐头!")


if __name__ == '__main__':
    # 子类重写方法后,调用是自己的重写的方法, 不调用父类的方法
    bsm = BoSiMao()
    bsm.sing()
    bsm.eat()
    bsm.catch()
