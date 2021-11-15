'''
使用while 循环打印 *
'''

'''
1.打印正方形
********
********
********
********
'''
i = 0  # 控制行
while i < 4:
    j = 0  # 控制列
    while j < 8:
        print('* ', end='')
        j += 1
    print()
    i += 1

'''
2.打印三角形
*
**
***
****
*****
'''
i = 0  # 控制行
while i <= 5:
    j = 0  # 控制列
    while j < i:  # 列数据不大于行数
        print('* ', end='')
        j += 1
    print()
    i += 1

'''
打印 99 乘法表
'''
print("_" * 80)
i = 1  # 控制行
while i <= 9:
    j = 1  # 控制列
    while j <= i:  # 列数据不大于行数
        #s = j * i
        # \t 表示Tab键,文本输出显示时保持对齐.
        print('%s*%s=%s\t' % (j, i, j*i), end='')
        j += 1
    print()
    i += 1