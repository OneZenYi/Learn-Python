'''
while 循环遍历容器
'''

val_list = ['1123', 112, 232, True, 12.32, (1, 3, 5)]

# 遍历列表数据, 列表名[定义变量名]
i = 0
while i <= 5:
    print(val_list[i])
    i += 1

# while 循环遍历容器需要通过索引
var_tuple = (1, 2, 3, 4, 5, 6, 7)
i = 0
while i < len(var_tuple):
    print(var_tuple[i])
    i += 1

