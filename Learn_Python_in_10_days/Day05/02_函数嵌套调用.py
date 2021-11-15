'''
函数嵌套调用
'''

def demo_01():
    print('函数demo_01开始')
    print('函数demo_01执行过程')
    print('函数demo_01结束')

def demo_02():
    print('函数demo_02开始')
    demo_01()
    print('函数demo_02执行过程')
    print('函数demo_02结束')

demo_02()