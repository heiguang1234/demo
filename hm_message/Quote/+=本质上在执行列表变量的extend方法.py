# 开发者：Hei guang
# 开发时间：2022/6/25 14:12


def demo(num, num_list):
    print("函数内部代码")
    # num=num+num
    num += num
    # num_list.extend(num_list)由于是调用的方法所以不会改变变量的引用
    # 函数执行后，外部数据同样会发生变化
    num_list += num_list

    print(num)
    print(num_list)
    print("函数代码完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
