# 开发者：Hei guang
# 开发时间：2022/6/28 17:13


# 操作文件三步骤
# 1 打开文件
file = open("readme")
# 2 读写文件
# read方法执行之后会将文件指针移动到文档末尾
text = file.read()
print(text)
print(len(text))
print("*" * 50)
print(file.read())
print(len(file.read()))
# 3 关闭文件
file.close()
