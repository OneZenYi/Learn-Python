"""
捕捉异常
"""

try:
    print(num)

except:
    print("报异常了")

"""
定义捕获异常
"""
try:
    print(num)
    int("hooll")

except NameError:
    print("捕获变量未定义异常")
except ValueError:
    print("捕获值异常")

print("_" * 50)
"""
一次捕获多个异常
"""

try:
    print(num)
    int("hooll")

except (NameError, ValueError):
    print("捕获变量未定义异常")

"""
捕获异常信息
"""

try:
    print(num)
    int("hooll")
# 取别名保存错误信息  as
except Exception as info:
    print(info)

"""
异常语法
"""
try:
    pass
except NameError:
    pass
except (Exception,ValueError):
    pass
except Exception:
    pass
else:
    pass
finally:
    pass
