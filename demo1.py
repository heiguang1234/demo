# 开发者：Hei guang
# 开发时间：2022/6/9 10:26


# lst=[i*2 for i in range(1,11)]
# print(lst)
# '''切片删除后'''
# lst[5:]=[]
# print(lst)
#

# 区分奇偶数列
# def split_(lst):
#     odd = []  # 存偶数
#     even = []  # 存奇数
#     for i in lst:
#         if i % 2 == 0:
#             odd.append(i)
#         else:
#             even.append(i)
#     return odd, even
#
#
# print(split_([1, 2, 4, 56, 7, 8, 9, 10]))

#默认值参数
def fun(a,b=10):
    print(a,b)

fun(10,20)