"""
私有属性与方法
"""


class Women:

    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 20

    def eat(self):
        print("%s是吃货,今年%s岁" % (self.name, self.__age))
        # 在类的内部能访问私有方法
        self.__secret()

    def __secret(self):
        """前置双下划线的是私有方法"""
        print("这事私有方法")


meinv = Women("小姐姐")
print(meinv.name)

meinv.eat()

print("_" * 50)
"""
伪私有属性,伪私有方法
"""


class Women_1:

    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 20

    def get_age(self):
        """获取私有属性"""
        return self.__age

    def set_age(self, new_age):
        """设置私有属性值"""
        if 0 <= new_age or new_age >= 120:
            self.__age = new_age

    def eat(self):
        print("%s是吃货,今年%s岁" % (self.name, self.__age))
        # 在类的内部能访问私有方法

    def __secret(self):
        """前置双下划线的是私有方法"""
        print("这事私有方法")


meinv = Women_1("小姐姐")
# 查看属性
dir(meinv)
print(meinv.name)
# 可以通过  _类名__私用属性名    _类名__私用方法名   访问私有方法
print(meinv._Women_1__age)
meinv._Women_1__secret()
meinv.eat()

# 修改属性值
print("_" * 50)
meinv.set_age(25)
r = meinv.get_age()
print(r)