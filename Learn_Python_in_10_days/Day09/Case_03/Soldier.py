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
        # while True:
            # 剩余子弹
        print("biu,biu,biu .剩余子弹数量:%d" % self.bullet_count)

        self.bullet_count -= 1




    def add_bullet(self, count):
        """添加子弹的方法"""
        self.bullet_count += count


class Soldier:
    """士兵类"""

    def __init__(self, name, gun=None):
        # 士兵名字
        self.name = name
        # 士兵默认配置没有枪,属于缺省参数
        self.gun = gun

    def add(self,new_count):
        """当期方法士兵拿抢添加子弹"""
        if self.gun == None:
            print("当前士兵没有抢哦!请领取枪!")
            return
        self.gun.add_bullet(new_count)

    def fire(self):
        # 判断士兵是否有抢
        # Python None 比较  用is  not is
        if self.gun is None:
            print("当前士兵没有抢哦!请领取枪!")
            return
        # 士兵有枪,需要添加子弹

        #self.gun.add_bullet(50)

        # 士兵拿抢射击
        self.gun.shoot()


ak47 = Gun("AK47")

xsd = Soldier("许三多", ak47)
xsd.add(50)
xsd.fire()
xsd.fire()
xsd.fire()
