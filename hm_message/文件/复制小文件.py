# 开发者：Hei guang
# 开发时间：2022/6/28 17:32

file = open("readme")
copyfile = open("readme01", "w")

text = file.read()
copyfile.write(text)

file.close()
copyfile.close()

