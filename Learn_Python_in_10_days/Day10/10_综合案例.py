"""
综合案例
"""


class Game:
    """游戏类"""
    # 类属性
    top_score = 0

    def __init__(self, playeer_name):
        """初始化方法"""
        # 游戏玩家
        self.playeer_name = playeer_name

    @staticmethod
    def show_help():
        """静态方法"""
        print("不能让僵尸走进房间!")

    @classmethod
    def show_top_score(cls):
        """类方法"""
        print("显示历史最高个分", cls.top_score)

    def start_game(self):
        print("游戏开始")
        print("%s  玩得很快乐!" % self.playeer_name)
        Game.top_score += 100


if __name__ == '__main__':
    # 显示帮助信息
    Game.show_help()
    # 查看历史最高分
    Game.show_top_score()
    # 创建对象,开始游戏
    xm = Game("小明")
    xm.start_game()
    # 查看历史最高分
    Game.show_top_score()
