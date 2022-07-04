# 开发者：Hei guang
# 开发时间：2022/6/14 22:21
# 记录所有的名片字典
card_list = []


def show_menu():
    '''显示菜单'''
    print("*" * 50)
    print("欢迎使用【名片管理系统】")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    '''新增名片'''
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name = input("请输入姓名：")
    phone = input("请输入电话号码：")
    qq = input("请输入QQ号：")
    email = input("请输入邮箱地址：")
    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name, "phone": phone, "qq": qq, "email": email}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户添加成功
    print("添加%s的名片成功！" % name)


def show_all():
    '''显示所有名片'''
    print("-" * 50)
    # 判断是否存在名片记录如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前系统中没有名片信息，请使用新增名片功能进行添加")
        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return后面没有任何内容，表示会返回到调用函数的位置
        # 并且不返回任何的结果
        return
    # 打印表头
    list = ["姓名", "电话", "QQ", "邮箱"]
    for _ in list:
        print(_, end="\t\t")
    print()
    print("=" * 50)
    for item in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (item["name"], item["phone"], item["qq"], item["email"]))


def search_card():
    '''搜索名片'''
    print("-" * 50)
    print("搜索名片")
    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入想要查找的人的姓名")
    # 2.便利名片系统，进行查询
    for item in card_list:
        if item["name"] == find_name:
            print("姓名\t\t", "电话\t\t", "QQ\t\t", "邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (item["name"], item["phone"], item["qq"], item["email"]))
            # TODO 针对查找的名片进行修改删除
            deal_card(item)
            break
    else:
        print("系统中没有%s" % find_name)


def deal_card(find_card):
    print(find_card)
    action_str = input("请输入想要进行的操作："
                       "[1] 修改 [2]删除 [0] 返回上级菜单")
    if action_str == "1":
        find_card["name"] = input_card_info(find_card["name"],"请输入修改的姓名：")
        find_card["phone"] = input_card_info(find_card["phone"],"请输入修改的电话：")
        find_card["qq"] = input_card_info(find_card["qq"],"请输入修改的QQ：")
        find_card["email"] = input_card_info(find_card["email"],"请输入修改的邮箱：")

        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_card)
        print("删除名片")
    else:
        return


def input_card_info(dict_value, tip_message):
    """

    :param dict_value:
    :param tip_message:
    :return:
    """
    # 1.提示用户输入内容
    result = input(tip_message)

    # 2.针对用户的输入进行判断，如果输入内容，直接返回结果
    if len(result) > 0:
        return result
    else:
        # 3.如果没有输入内容，返回字典中原有的值
        return dict_value
