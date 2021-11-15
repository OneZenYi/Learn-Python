"""
操作文件
"""
# 打开文件,指定编码格式 encoding
file = open("test.txt", encoding="utf8")
# 读取文件
text = file.read()
print(text)
# 关闭文件
file.close()

"""
打开文件方式
"""
# mode="r"  写 文件操作方式  r w a r+ w+  a+
file = open(file="test.txt", mode="r", encoding="utf8")
text = file.read()
print(text)
# 关闭文件
file.close()
print("*" * 50)

# mode="w"  读 文件操作方式  r w a r+ w+  a+
file = open(file="test.txt", mode="w", encoding="utf8")
# 写入文件内容
text = file.write("马上去吃饭!\n123123123\n我很辣鸡!")
print(text)
# 关闭文件
file.close()
print("*" * 50)

# mode="a"  追加 文件操作方式  r w a r+ w+  a+
file = open(file="test.txt", mode="a", encoding="utf8")
# 写入文件内容
text = file.write("马上去吃饭!\n123123123\n我很辣鸡!")
print(text)
# 关闭文件
file.close()
print("*" * 50)

"""
按行对齐文件内容   rendline()读取大文件内容
"""

file = open(file="test1.txt", mode="r", encoding="utf8")
# 写入文件内容
# 遍历文件夹每一行
while True:
    # 读取一行
    text = file.readline()
    # 结算死循环
    if len(text) == 0:
        break
    print(text)
# 关闭文件
file.close()

"""
复制文件
"""
# 原始文件
file = open("test.txt", "r", encoding="utf8")
# 复制新文件
file_1 = open("copy.txt", "w", encoding="utf8")

# 读取文件
text = file.read()
# 写人数据
file_1.write(text)

# 关闭文件
file.close()
file_1.close()

"""
大文件复制文件
"""
# 原始文件
file = open("test.txt", "r", encoding="utf8")
# 复制新文件
file_1 = open("copy_1.txt", "w", encoding="utf8")

while True:

    # 读取文件
    text_1 = file.readline()

    # 写人数据
    file_1.write(text_1)
    if len(text_1) == 0:
        break

# 关闭文件
file.close()
file_1.close()
