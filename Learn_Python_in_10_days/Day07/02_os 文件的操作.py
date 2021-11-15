import os

# 修改文件名
# os.rename("test1.txt", "test2.txt")

# 删除文件
# os.remove("")


"""
os 对目录的操作
"""
# 获取所有目录
listdir = os.listdir(".")
listdir1 = os.listdir("./")

# listdir2=os.listdir("\\Users\\mantis\\Documents\\Learn-Python\\Learn_Python_in_10_days")
print(listdir, listdir1)

# 创建目录
# os.mkdir("/Users/mantis/Documents/Learn-Python/Learn_Python_in_10_days/Day08")

import shutil

# 删除目录   rmdir 只能删除空目录
# os.rmdir("/Users/mantis/Documents/Learn-Python/Learn_Python_in_10_days/Day08")
# 可以删除非空目录
# shutil.rmtree("")

# 获取当前目录
print(os.getcwd())

# 修改工作目录
# os.chdir("")

# path.isdir 判断是否是文件夹
print(os.path.isdir("/Users/mantis/Documents/Learn-Python/Learn_Python_in_10_days/Day07/test2.txt"))

# os.path.exists()  判断目录与文件是否存在
print(os.path.exists("/Users/mantis/Documents/Learn-Python/Learn_Python_in_10_days/Day07/test2.txt"))