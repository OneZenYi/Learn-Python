"""
class 类名 (父类名):
"""


class Animal:
    """动物类,父类"""

    def __init__(self):
        self.name = "动物"
        self.age = 2

    def eat(self):
        print("%s 都爱吃东西" % self.name)


class Cat(Animal):
    """单继承,动物类"""

    def catch(self):
        print("猫抓老鼠")


if __name__ == '__main__':
    animal = Animal()
    print(animal.name)
    print(animal.age)
    # 父类对象可以调用自己的方法
    animal.eat()

    print("*" * 50)
    # 子类方法调用父类 属于与方法
    cat = Cat()
    print(cat.name)
    print(cat.age)
    cat.eat()
