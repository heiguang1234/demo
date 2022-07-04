# 开发者：Hei guang
# 开发时间：2022/6/28 17:18

# open方法默认以只读方式打开文件，并且返回文件对象
# 语法如下
# f=open（"文件名"，"访问方式"）

# 1.打开文件
file = open("readme","a")
# 2.写入文件
file.write("带笑颜是sb")
# 3.关闭文件
file.close()
