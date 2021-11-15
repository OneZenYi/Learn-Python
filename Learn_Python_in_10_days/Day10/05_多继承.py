"""
多继承
"""


class Donkey:
    """驴类"""

    def walk(self):
        print("驴打转!")


class Hores:
    """马类"""

    def run(self):
        print("千里马,跑得块!")


# 多继承  类名(类名1,类名2,....)  多继承可以访问父类私所有属性与方法,不能访问私有属性与方法
class Mule(Donkey, Hores):
    """骡子类"""
    pass


if __name__ == '__main__':
    lz = Mule()
    lz.walk()
    lz.run()
