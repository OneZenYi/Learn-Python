str_1 = 'hello,python,Python,java'
print(str_1.split(','))
new_str = str_1.split(',')  # 通过列表替换
new_str[2] = 'go'
new_str_join = ','.join(new_str)  # 用 join 拼接
print(new_str_join)

# partition() 从左到右 ,rpartition()从右到左  拆分
print(str_1.partition('Python'))
t=str_1.partition('Python')
new_list=list(t)
print(new_list)
new_list[1]='go'
print(new_list)
new_list=','.join(new_str)
print(new_list)