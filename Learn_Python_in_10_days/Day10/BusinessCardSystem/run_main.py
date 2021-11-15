"""
主方法,调用所以的方法与函数
"""
import card_tool


class RunMain:
    """总控中心类"""

    # card_tool.show_card_menu()
    def __init__(self):
        """初始化方法"""
        # 创建对象
        self.ct = card_tool.CardTool()
        self.ct.read_file()

    def run(self):
        while True:
            # 显示名片管理系统菜单
            self.ct.show_card_menu()

            action = input("请输入您的选择项:")
            # print("你输入的项目为s%" % action)

            if action in ['1', '2', '3']:
                if action == '1':
                    # 新增名片
                    self.ct.new_card()
                elif action == '2':
                    # 显示全部名片
                    self.ct.display_all_card()
                else:
                    # 查询名片
                    self.ct.check_card()
                pass
            elif action == '0':
                # 保存名片
                self.ct.save_file()
                # 退出名片系统
                print('退出系统成功!欢迎再次使用名片管理系统!')
                break
            else:
                print("输入错误!请重新输入!")


if __name__ == '__main__':
    mp = RunMain()
    mp.run()
