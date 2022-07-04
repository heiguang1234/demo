# 开发者：Hei guang
# 开发时间：2022/6/28 17:43

# 读文件
file = open("readme")
copyfile = open("readme02", "w")
while True:
    # 读取一行内容
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    copyfile.write(text)
# 关闭文件
file.close()
copyfile.close()
