'''
元组
'''
# 一个数据元组定义  元组名=(数据,)
# 元组是有序,可以通过索引访问
# 元组里面的数据不能修改
tuple_1 = (1, 2, 3, 4, 'zhangy', False)
print(len(tuple_1))
print(tuple_1[4])  # 索引越界会报错

# 通过索引获取数据  元组名[索引]
# 通过数据获取索引  元组名.index(数据值)
# 通过数据出现次数  元组名.count(数据值)
# 添加元组字符长度  len(元组名)
