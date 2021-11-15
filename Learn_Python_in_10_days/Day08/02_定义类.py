"""
定义简单类
"""


# 新增类名
class Person:
    # 新增函数
    def run(self):
        print("运动一下!")

    def eat(self,food):
        print("吃什么饭哦!%s" % food)


"""
使用类,创建对象 , 变量名=类名()
"""
# 创建对象
xiaomi = Person()

# 通过对象调用方法,对象变量名.方法名()
xiaomi.eat("吃汉堡")
xiaomi.run()
