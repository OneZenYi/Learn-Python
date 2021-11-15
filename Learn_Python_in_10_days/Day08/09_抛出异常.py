"""
抛出异常
"""


def input_password():
    pwd = input("输入密码:")

    if len(pwd) < 8:
        # Exception 捕获异常
        exp = Exception("密码长度小于8位")
        # raise 抛出异常
        raise exp
    else:
        return pwd


try:
    input_password()
except Exception as exp:
    print(exp)
