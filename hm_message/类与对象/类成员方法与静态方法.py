# 开发者：Hei guang
# 开发时间：2022/6/25 17:04


# 类的方法分有不同种类主要有
# 实例方法
# 类方法
# 静态方法
# 静态方法用@staticmethod修饰
# 静态方法的定义要不涉及属性的变换和其他非静态方法的调用
# 类方法用@classmethod修饰且必须有默认参数cls
# 类方法在方法内部可以访问类属性调用其他类方法
class DemoMthd:

    @staticmethod
    def static_mthd():
        DemoMthd.static_mthd01()
        print("调用了静态方法")

    @staticmethod
    def static_mthd01():
        print("二次调用静态方法")

    @classmethod
    def class_method(cls):
        print("调用了类方法")


DemoMthd.static_mthd()
