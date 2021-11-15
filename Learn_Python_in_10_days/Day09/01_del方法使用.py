"""
__del__  方法  对象从内存空间销毁前,自动调用 (当前程序退出时)  清除资源操作
"""


class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃鱼儿" % self.name)
        self.file=open ("tx1t.txt","w",encoding="utf8")
        self.file.write("%s 爱吃鱼儿" % self.name)

    # 在程序退出之前自动调用
    def __del__(self):
        print("清除资源")
        self.file.close()


tom = Cat("哈哈")
tom.eat()
