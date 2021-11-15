"""
名片系统优化
"""
import os.path

list_card = []


# 显示菜单
def show_card_menu():
    """
    显示名片菜单功能
    :return:
    """
    print()
    print("*" * 20 + " 欢迎使用名片管理系统 " + "*" * 20)
    print()
    print("1.新增名片")
    print("2.显示全部名片")
    print("3.查询名片")
    print()
    print("0.退出名片系统")
    print("*" * 20 + " 欢迎使用名片管理系统 " + "*" * 20)


# 新建名片
def new_card():
    """
    新增名片功能
    :return:
    """
    print("*" * 20 + " [功能]新增名片 " + "*" * 20)
    # 输入名片信息
    name = input("请输入您的名字:")
    Phone = input("请输入您的电话:")
    qq = input("请输入您的QQ号:")
    email = input("请输入您的邮箱:")
    # 保存名片信息在字典里中
    new_dict = {
        'name': name,
        'Phone': Phone,
        'qq': qq,
        'email': email
    }
    # 条件字典到列表
    list_card.append(new_dict)
    # 打印新增名片成功
    print("新增 %s 名片成功!" % name)
    print("名片列表:", list_card)


# 显示全部名片
def display_all_card():
    """
    显示全部名片
    :return:
    """
    print("*" * 20 + " [功能]显示全部名片 " + "*" * 20)
    if len(list_card) <= 0:
        print("当前名片没有数据, 请新增名片!")
        return
    else:
        print('_' * 50)
        # ljust(10) 左对齐
        print("姓名".ljust(8), "电话".ljust(8), "QQ号".ljust(10), "邮箱".ljust(8), sep="\t\t")
        print('_' * 50)
    for i in list_card:
        print(i.get("name").ljust(8), i.get("Phone").ljust(8), i.get("qq").ljust(8), i.get("email").ljust(8),
              sep="\t\t")
        # i.get("Phone")


# 查询名片
def check_card():
    """
    查询名片
    :return:
    """
    print("*" * 20 + " [功能]查询名片 " + "*" * 20)
    name = input("请输入查询名片名字:")
    for i in list_card:
        if name == i.get("name"):
            # print("找到了%s的名片信息!", i.get("name"))
            print('_' * 50)
            # ljust(10) 左对齐
            print("姓名".ljust(8), "电话".ljust(8), "QQ号".ljust(10), "邮箱".ljust(8), sep="\t")
            print('_' * 50)
            print(i.get("name").ljust(8), i.get("Phone").ljust(8), i.get("qq").ljust(8), i.get("email").ljust(8),
                  sep="\t")
            print('_' * 50)
            deal_card(i)
            break
        else:
            print()
            print("无法找到您搜索%s的名片信息!", i.get("name"))


# 操作名片 (修改\删除\返回)
def deal_card(find_card):
    """
    操作名片 (修改\删除\返回)
    :return:
    """
    print("*" * 20 + " 修改名片 " + "*" * 20)
    i = input("请输入对名片的选择:[1]-修改名片,[2]-删除名片,[0]-返回菜单")

    if i == "1":
        print("*" * 20 + " [功能]修改名片 " + "*" * 20)
        # 替换修改后的数据
        find_card["name"] = input_card_info(find_card.get("name"), "请输入修改后名字[不修改直接回车]:")
        find_card["Phone"] = input_card_info(find_card.get("Phone"), "请输入修改后电话[不修改直接回车]:")
        find_card["qq"] = input_card_info(find_card.get("qq"), "请输入修改后QQ号[不修改直接回车]:")
        find_card["email"] = input_card_info(find_card.get("email"), "请输入修改后邮箱[不修改直接回车]:")

        print("修改名片成功!")

    elif i == "2":
        print("*" * 20 + " [功能]删除名片 " + "*" * 20)
        list_card.remove(find_card)
        print("删除成功")
    elif i == "0":
        return
    else:
        print()
        print("输入有误, 请重新输入!")


# input 扩展
def input_card_info(find_card, msg):
    pass
    # 获取用户输入信息
    info = input(msg)
    # 对用户的输入信息判断

    # 如果input 有输入信息,把输入信息返回字典
    if len(info) > 0:
        # print("有输入信息%s" % info)
        return info
    # 如果input 没有输入信息,不能返回空
    else:
        # print("没有输入信息%s" % info)
        return find_card


# 将列表写入文件中
def save_file():
    file = open("card.txt", "w", encoding="utf8")
    file.write(str(list_card))
    file.close()


# 将列表读取文件中
def read_file():
    if os.path.exists("card.txt"):
        file = open("card.txt", "r", encoding="utf8")
        text = file.read()

        if len(text) == 0:
            file.close()
            return
        else:
            #  给全局变量赋值
            global list_card
            list_card = eval(text)

        file.close()
    else:
        os.mkdir("card.txt")

# 主方法
# if __name__ == '__main__':
#     while True:
#         # 显示名片管理系统菜单
#         show_card_menu()
#
#         action = input("请输入您的选择项:")
#         # print("你输入的项目为s%" % action)
#
#         if action in ['1', '2', '3']:
#             if action == '1':
#                 # 新增名片
#                 new_card()
#             elif action == '2':
#                 # 显示全部名片
#                 display_all_card()
#             else:
#                 # 查询名片
#                 check_card()
#             pass
#         elif action == '0':
#             # 退出名片系统98
#             print('退出系统成功!欢迎再次使用名片管理系统!')
#             break
#         else:
#             print("输入错误!请重新输入!")
