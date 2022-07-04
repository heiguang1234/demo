# 开发者：Hei guang
# 开发时间：2022/7/2 21:37
# 表示文件只在本python文件中进行使用，并不会被其他文件进行调用
import requests

if __name__ == "__main__":
    # 1.指定url
    url = "https://www.baidu.com"
    # 2.发起请求
    # get方法会返回一个响应对象
    response = requests.get(url)
    # 3.获取响应数据 text返回的是字符串数据的响应数据
    page_text = response.text
    print(page_text)
    # 4.持久化存储
    with open("./baidu.html", "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print("爬取数据结束")
