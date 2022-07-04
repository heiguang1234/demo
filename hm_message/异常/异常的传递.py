# 开发者：Hei guang
# 开发时间：2022/6/27 11:54
# 异常的传递--当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方
# 如果传递到主程序，仍然没有异常处理，程序才会被终止

def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo1())
except Exception as result:
    print("未知错误%s" % result)
