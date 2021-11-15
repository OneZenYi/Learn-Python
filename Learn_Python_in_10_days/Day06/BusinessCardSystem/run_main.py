"""
主方法,调用所以的方法与函数
"""
import card_tool

# card_tool.show_card_menu()

while True:
    # 显示名片管理系统菜单
    card_tool.show_card_menu()

    action = input("请输入您的选择项:")
    # print("你输入的项目为s%" % action)

    if action in ['1', '2', '3']:
        if action == '1':
            # 新增名片
            card_tool.new_card()
        elif action == '2':
            # 显示全部名片
            card_tool.display_all_card()
        else:
            # 查询名片
            card_tool.check_card()
        pass
    elif action == '0':
        # 退出名片系统98
        print('退出系统成功!欢迎再次使用名片管理系统!')
        break
    else:
        print("输入错误!请重新输入!")
