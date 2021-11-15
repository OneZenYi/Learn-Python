class Cat:
    """猫类"""

    def eat(self):
        """
        吃方法
        :return:
        """
        print("我爱吃鱼!", self)

    def drink(self, water):
        """
        喝方法
        :return:
        """
        print("我爱喝水!:%s" % water)

# 调用方法
tom_eat = Cat()
tom_eat.eat()
tom_drink = Cat()
tom_drink.drink("牛奶")
