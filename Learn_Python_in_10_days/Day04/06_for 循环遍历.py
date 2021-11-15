'''
for 循环遍历四大容器 字符串,列表,元组,字典
'''

'''
格式: for 临时变量 in 容器:
          处理临时变量
          '''
val_list = ['1123', 112, 232, True, 12.32, (1, 3, 5)]

for i in val_list:
    if i == 12.32:
        print("找到了12.32")
    else:
        print(i)

print('_' * 50)

# 临时变量获取字典获取字典键,需要获取值的格式  (临时变量,变量名[临时变量])  (临时变量,变量名.get(临时变量))
val_ditc = {'123': 123, 'name': '张珊'}
for i in val_ditc:
    print(i, val_ditc.get(i))

print('_' * 50)

'''
for 循环的完整语法

语法格式
for ... else ... 
'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]

for i in list_1:
    if i == 8:
        print(i)
        break
else:
    print('没有想要的!')

print('_' * 50)

'''
for 循环 应用场景
'''
list_1 = [{'name': '小米', 'age': 18, 'high': 172.52}, {'name': '小狗', 'age': 28, 'high': 152.15},
          {'name': '小名', 'age': 48, 'high': 126.35}]
name = '小名'
for i in list_1:
    print(i.get('name'))
    if i.get('name') == name:
        print('_' * 50)
        print('找到了:%s' % name)
        print('姓名:%s,身高:%s,年龄:%s,'% (i.get('name'),i.get('high'),i.get('age')))
        break
else:
    print('没有找到哦!')
