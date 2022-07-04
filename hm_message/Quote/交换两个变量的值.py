# 开发者：Hei guang
# 开发时间：2022/6/25 13:04


# a = 10
# b = 20
#
#
# def swap():
#     global a
#     global b
#     temp = a
#     a = b
#     b = temp
#
#
# swap()
# print("a=%s,b=%d" % (a,b))
# print(type(print("%d"%b)))
a = 6
b = 100
# 解法1
c = a
a = b
b = c
# 解法2 不使用其他变量
a = a + b
b = a - b
a = a - b

# 解法3 python 专有 等号右边是一个元组，只是把小括号省略了
a, b = b, a
