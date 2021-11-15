'''
字典   1.字典是无序的  2.字典的key不能是列表或字典本身
'''

# 字典定义   字典名={key:value,key:value}    空字典:字典名={}  或 字典名=dict()

dict_1 = {
    'name': '小米',
    'age': 29,
    'gender': '女',
    'high': 179.23
}
print(dict_1)

# 字典访问,通过key 访问,不能通过索引访问
print(dict_1['age'], dict_1['high'])

# 字典查  字典名[key]    字典名.get(key)
# 字典不存在的key,会报错
dict_2 = {
    'name': '小米',
    'age': 29,
    'gender': '女',
    'high': 179.23
}
print(dict_2['gender'])
# 开发常用方法 字典名.get(key)
print(dict_2.get('name'))

# 增/改  字典名[key] = 修改值
print(dict_2.get('name'))
dict_2['name'] = '小姐姐'
print(dict_2)
dict_2['addr'] = '上海市浦东新区'
print(dict_2)

# 字典名.setdefault(key,value) 使用默认
print(dict_2.setdefault('name', '小姐姐123'))
print(dict_2.setdefault('addr', '上海市浦东新区'))

# 字典名.update(字典)
dict_2.update({
    'name': '小米1',
    'age': 129,
    'gender': '1女1',
    'high': 1179.23,
    'addr': '上海市浦东新区'
})
print(dict_2)

# 字典删除操作  del 字典名[key]  字典名.pop(key)  字典名.clear()
dict_3 = {
    'name': '小米1',
    'age': 129,
    'gender': '1女1',
    'high': 1179.23,
    'addr': '上海市浦东新区'
}
# del 字典名[key]
del dict_3['name']
print(dict_3)
# 字典名.pop(key)
dict_3.pop('gender')
print(dict_3)
# 字典名.clear()
dict_3.clear()
# 统计长度
print(len(dict_2))
