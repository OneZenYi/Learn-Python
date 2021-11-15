class Cat:

    # 初始化方法
    # 传参
    def __init__(self, name_1):
       # print("123123")
        self.name = name_1

    def eat(self):
        print("%s 吃鱼干" % self.name)


tom = Cat("大蓝莓")
tom.eat()

boasm=Cat("哈哈猫")
boasm.eat()
