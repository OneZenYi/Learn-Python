class Gun:
    """抢类"""

    def __init__(self, type):
        """初始化数据"""

        # 抢类型
        self.type = type
        # 子弹的数据量
        self.bullet_count = 0
        pass

    def shoot(self):
        """射击方法"""

        # 判断是否有子弹,如果没子弹,提示请添加子弹.
        if self.bullet_count <= 0:
            print("如果没子弹,提示请添加子弹!")
            return
        # 打掉的子弹
        self.bullet_count -= 1
        # 剩余子弹
        print("biu,biu,biu .剩余子弹数量:%d" % self.bullet_count)

    def add_bullet(self, count):
        """添加子弹的方法"""
        self.bullet_count += count

# ak47 = Gun("AK47")
# ak47.add_bullet(50)
# ak47.shoot()
