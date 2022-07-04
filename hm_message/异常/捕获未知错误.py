# 开发者：Hei guang
# 开发时间：2022/6/27 11:23
# 在开发时，要预判所有可能出现的错误
# 如果希望程序无论出现什么错误，都不会因为python解释器抛出异常而终止，可以再增加一个except
try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个整数："))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num
    print(result)

except ValueError:
    print("请输入正确的整数")
# python解释器抛出异常时，最后一行错误信息的第一个单词，就是错误类型
except Exception as result:
    # 捕获未知错误的语法
    print("未知错误%s" % result)
