from Learn_Python_in_10_days.Day09.Case_02.Houseitem import bed, chest, tale

print("_" * 50)


class House:

    def __init__(self, house_type, area):
        # 户型
        self.house_type = house_type
        # 总面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具
        self.item_list = []

    def __str__(self):
        return "户型:%s,总面积:%.2f,剩余面积:%.2f,家具名称列表:%s" % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        if self.free_area < item.area:
            print("添加:%s 家具面积过大,无法添加" % item.name)
            return
        # 更新房子剩余面积
        self.free_area -= item.area
        # 将家具保存在家具名称
        self.item_list.append(item.name)


big_huose = House("大洋房", 10)
print(big_huose)
big_huose.add_item(bed)
print(big_huose)
big_huose.add_item(chest)
print(big_huose)
big_huose.add_item(tale)
print(big_huose)
