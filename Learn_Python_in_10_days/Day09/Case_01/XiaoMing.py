class XiaoMing:

    def __init__(self, name, weight):
        """初始化方法"""
        self.name = name
        self.weight = weight

    def __str__(self):
        """打印描述信息"""
        return "名字是:%s 体重是:%.2f" % (self.name, self.weight)

    def run(self):
        print("名字是:%s 每次跑步减0.5公斤" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("名字是:%s 每次吃饭增加1公斤" % self.name)
        self.weight += 1


# 初始化数据
xiaoming = XiaoMing("嚣张", 75.0)
print(xiaoming)
# 跑步后数据
xiaoming.run()
print(xiaoming)
# 吃饭后数据
xiaoming.eat()
print(xiaoming)

print("_" * 50)
# 初始化数据
xiaomei = XiaoMing("小美", 65.0)
print(xiaomei)
# 跑步后数据
xiaomei.run()
print(xiaomei)
# 吃饭后数据
xiaomei.eat()
print(xiaomei)
