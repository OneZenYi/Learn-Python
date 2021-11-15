import os
import shutil


# 批量创建文件
def create_file():
    # 创建文件夹
    if os.path.exists("./Test_demo"):
        shutil.rmtree("./Test_demo")
    os.mkdir("./Test_demo")

    # 切换工作目录
    os.chdir("/Users/mantis/Documents/Learn-Python/Learn_Python_in_10_days/Day07/Test_demo")
    print(os.getcwd())

    # 批量删除文件
    for i in range(1, 21):
        # file= open("test"+str(i)+".txt","w",encoding='utf8')
        file = open("test%d.txt" % i, "w", encoding='utf8')
        file.write("测试一下")
        file.close()

# 批量修改名字
def update_file():
    print(os.getcwd())
    path ="/Users/mantis/Documents/Learn-Python/Learn_Python_in_10_days/Day07/Test_demo"

    # 判断是否在工作目录
    if os.getcwd()!=path:
        os.chdir(path)

    file_name=os.listdir()
    print(file_name)
    # 批量修改名字
    for name in file_name:
        os.rename(name,"py_"+name)


create_file()
update_file()