# 开发者：Hei guang
# 开发时间：2022/6/25 16:45

# 默认继承系统中自建的object类


'''类的方法的定义'''


# 方法的第一个参数必须是self，且不能省略 方法调用时不用提供self参数
# 方法的调用需要先实例化
class SimpleClass:
    def info(self):
        print("我定义的类")

    def mycacl(self, x, y):
        return x + y


sc = SimpleClass()
print("调用info方法的结果：")
sc.info()
print("调用mycacl方法的结果")
sc.mycacl()

'''定义类的格式'''


# 定义一个类的格式
# ()内是该类继承的父类名称
class Myclass(SimpleClass):
    pass
