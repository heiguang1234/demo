# 开发者：Hei guang
# 开发时间：2022/6/30 21:22

import urllib.request

# 使用urllib来获取百度首页的源码


# (1)定义一个url
url = "https://csdn.com"

# (2)模拟浏览器向服务器发送请求 response响应

response = urllib.request.urlopen(url)

# (3)响应中的页面源码
# read 方法 返回的是字节形式的二进制数据
# 我们要将二进制数据转化成字符串
# 二进制--》字符串 解码 decode("编码格式")
content = response.read().decode("utf-8")

# 打印数据
print(content)
