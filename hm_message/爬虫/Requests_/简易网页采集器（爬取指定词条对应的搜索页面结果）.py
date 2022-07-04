# 开发者：Hei guang
# 开发时间：2022/7/2 21:58

# UA：User——Agent(请求载体的身份标识)
# UA检测：门户网站的服务器回检测对应请求的载体身份标识，如果检测到请求的载体身份标识为一款浏览器
# 说明请求是一个正常的请求，但是如果检测到的身份标识不是浏览器则是不正常的请求，则服务器端可能拒绝该次请求

# UA伪装：让爬虫对应的请求载体身份标识伪装成一款浏览器
import requests

if __name__ == "__main__":
    # UA伪装：将对应的User-Agent封装到一个字典中去
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    url = "https://www.sogo.com/web"
    # 处理url携带的参数：封装到字典中
    kw = input("enter a word：")
    param = {
        "query": kw
    }
    # 对指定的url发起请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url, param, headers=headers)

    page_text = response.text
    fileName = kw + ".html"
    with open(fileName, "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print(fileName+"保存成功")
