# 开发者：Hei guang
# 开发时间：2022/6/28 17:25

# read方法会把文件所有内容一次性读取到内存中
# 如果文件太大，将对内存造成很严重的占用

# readline()方法可以一次读取一行的内容
# 方法执行后，会把文件指针移动到下一行，准备再次读写

file = open("readme")
while True:
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)

file.close()
