# 开发者：Hei guang
# 开发时间：2022/6/27 11:06


try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个整数："))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num
    print(result)
except ZeroDivisionError:  # 除0错误
    # 错误的处理代码
    print("除0错误")
except ValueError:
    print("请输入正确的整数")
# python解释器抛出异常时，最后一行错误信息的第一个单词，就是错误类型
