"""
家具类
"""


class Houseitem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具名字:%s  占地面积:%.2f" % (self.name, self.area)


bed = Houseitem("席梦思", 4)
print(bed)
chest = Houseitem("衣柜", 2)
print(chest)
tale = Houseitem("餐桌", 3.5)
print(tale)
