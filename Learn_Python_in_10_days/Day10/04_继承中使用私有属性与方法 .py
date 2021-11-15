"""
继承中使用私有属性与方法
"""


class Father:

    def __init__(self):
        """初始化方法"""

        self.name = "老王"
        self.__password = 888888

    def eat(self):
        """吃方法"""
        print("%s 爱吃老干妈!" % self.name)

    def __secre(self):
        """私有方法"""
        print("%s 老王的密码是:%d" % (self.name, self.__password))

    def get_pwd(self):
        return self.__password

    def set_pwd(self, new_pwd):
        self.__password = new_pwd

    def func_secret(self):
        """调用私有方法"""
        self.__secre()

class Son(Father):

    def run(self):
        print("小王喜欢旅游!")


if __name__ == '__main__':
    xw = Son()
    print(xw.name)
    print(xw.get_pwd())
    xw.set_pwd(12345678)
    print(xw.get_pwd())
    xw.func_secret()