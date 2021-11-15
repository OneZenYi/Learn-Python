'''
列表数据类型
'''

# 列表用 索引访问,索引不能越界
list_1 = ['zhangiii', '13142999972']

# 空列表定义
list_2 = list()

# 读取列表数据
print(list_1[1], list_1[0])
print(type(list_1))

# 列表增删改查

list_3 = ['1', 2, 'haha', 123, 26]

# 新增 字符串 insert(索引,增加值)
list_3.insert(3, 'kaixin')
print(list_3)
# 插入列表
list_3.insert(3, ['kaixin', 123])
print(list_3)

# append() 末尾追加数据
list_3.append([12311, 1000])
print(list_3)

# extend()
list_11 = ["111", 111]
list_12 = [100, 2000]
list_11.extend(list_12)
print(list_11)

# 删除列表  del(索引) remove(数据) pop()删除末尾数据 pop(索引)  clear()清空列表

list_del_1 = ['1', 2, '3', 4, 5, 6, 7, 8, 9]
# del 删除,索引不能越界
del list_del_1[0]
print(list_del_1)
# remove 删除,填写数据源
list_del_1.remove(2)
print(list_del_1)
# pop()删除末尾数据
num = list_del_1.pop()
print(num)
print(list_del_1)
# pop(索引)删除数据,索引不能越界
num_1 = list_del_1.pop(0)
print(num_1)
print(list_del_1)
# clear 清空列表
list_del_1.clear()
print(list_del_1)

# 列表修改  列表[索引]=修改值
list_xg = [1, 2, 3, 4]
list_xg[0] = 12
print(list_xg)

# 查询列表数据  列表[索引]
print(list_xg[0])

# 通过数据获取索引  列表.index(列表值)
print(list_xg.index(3))


list_01=[1,2,23,25,2,35,22,1,23,65,6,7,89,21,16,23]
# 统计列表长度  len.(列表)
print(len(list_01))

# 统计列表里面的次数 列表.count()
print(list_01.count(2))
print(list_01.count(23))

# 列表排序  列表.sort()
list_01.sort()
print(list_01)

# 列表逆序  列表.reverse()
list_01.reverse()
print(list_01)

# 列表拷贝 列表.copy()
list_01.copy()


