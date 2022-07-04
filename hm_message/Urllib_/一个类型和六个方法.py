# 开发者：Hei guang
# 开发时间：2022/6/30 21:42
import urllib.request

url = "http://www.baidu.com"

# 模拟浏览器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))


# 按照一个字节一个字节去读
content = response.read().decode("utf-8")
print(content)

# 返回多少个字节
content = response.read(5)

# 读取一行
content = response.readline()

# 一行一行读直到结束
content = response.readlines()

# 返回状态码
print(response.getcode())

# 返回url地址
print(response.geturl())

# 获取的是一个状态信息
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read readline readlines getcode geturl getheaders
