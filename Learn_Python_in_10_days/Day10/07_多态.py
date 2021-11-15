"""
多态: 成立条件
1.要有继承
2.要有方法重写
3.又有分类的对象或子类的对象作为方法的参数
"""


class Dog:
    """普通狗类"""

    def __init__(self, name):
        """初始化方法"""
        self.name = name

    def game(self):
        """玩游戏的方法"""
        print("%s 在地上玩耍" % self.name)


class Xtq(Dog):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s在天上玩耍" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def play_dog(self, dog):
        """和狗玩的方法"""
        print("%s 和 %s 狗一起玩耍" % (self.name, dog.name))
        # 不同的对象,调用相同的方法,产生不同的结果状态,叫多态
        dog.game()


if __name__ == '__main__':
    # 普通狗类创建对象
    pt = Dog("旺财")

    # 哮天犬类创建对象
    xtq = Xtq("哮天犬")

    # 人类创建对象
    cw = Person("成为")

    cw.play_dog(xtq)
    print("*" * 50)
    cw.play_dog(pt)
