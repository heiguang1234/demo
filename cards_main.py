# 开发者：Hei guang
# 开发时间：2022/6/14 22:21
import cards_tools


while True:
    # 显示功能菜单
    cards_tools.show_menu()
    action = int(input("请输入想要的功能："))
    print("您选择的操作是%s" % action)
    # 新增名片
    if action == 1:
        cards_tools.new_card()
    # 显示全部
    elif action == 2:
        cards_tools.show_all()
    # 查询名片
    elif action == 3:
        cards_tools.search_card()
    # 退出系统
    elif action == 0:
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("你的操作不正确")
