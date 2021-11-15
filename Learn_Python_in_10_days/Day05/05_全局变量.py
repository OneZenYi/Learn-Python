'''
全局变量
'''

g_num=100
def demo_01():
    # 修改全局变了,必须添加 global关键字
    global g_num
    g_num=1000
    print(g_num)

def demo_02():
    print(g_num)


demo_01()