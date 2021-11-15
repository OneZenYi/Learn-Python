"""
类方法,叫装饰器
"""


# @classmethod  # 是装饰器,修饰器 对函数和方法进行添加功能(在不修改函数的源代码的前提下,个函数或方法添加功能,要么在函数调用之前添加,要么在函数调用之后添加)
# def 类名(cls):  # cls 调用类方法引用

class Person(object):
    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃美食!" % self.name)

    @classmethod
    def get_count(cls):
        """这是类方法"""
        print("处理类属性,或调用其他方法")
        print("cls 参数保存当前类对象的引用", cls)
        cls.count += 100
        return cls.count

    @staticmethod
    def func_static():
        """静态方法"""   # 静态方法 不需要self 与cls 参数, 不需要属性,方法
        pass
        # 调用静态方法    类名.静态方法名()  实例对象.静态方法名()

if __name__ == '__main__':
    print("Person:", Person)

    r = Person.get_count()
    print(r)
