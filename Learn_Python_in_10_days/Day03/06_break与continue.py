'''
break  与 continue
'''

# break
i = 1
while i <= 5:
    print("打印i的次数:%s" % i)
    if i == 3:  # break 提前终止 while 循环
        break
    i += 1

print('-' * 50)
# continue
i = 1
while i <= 5:
    i += 1  # 修改循环变量必须放在continue之前, 如果是之后会出现死循环
    if i == 3:  # continue 跳过本次循环,执行下一次循环
         continue
    print("打印i的次数:%s" % i)
