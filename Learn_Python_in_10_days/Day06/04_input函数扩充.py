def input_card_info(msg):
    pass
    # 获取用户输入信息
    info=input(msg)
    # 对用户的输入信息判断

    # 如果input 有输入信息,把输入信息返回字典
    if len(info) > 0:
        print("有输入信息:%s" % info)
        return info
    # 如果input 没有输入信息,不能返回空
    else:
        print("没有输入信息:%s" % info)
        return "返回默认值"

ret =input_card_info("请输入用户信息:")
print("请输入用户信息:%s" % ret)