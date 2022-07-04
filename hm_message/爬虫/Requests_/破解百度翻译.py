# 开发者：Hei guang
# 开发时间：2022/7/2 22:37
import requests
import json
if __name__ == "__main__":
    # 1.指定url
    post_url = "https://fanyi.baidu.com/sug"
    # 2.进行UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    # 3.post请求参数处理
    word=input("enter a word:")
    data = {
        "kw": word
    }
    # 4.请求发送
    response=requests.post(post_url, data=data, headers=headers)
    # 5.获取响应数据: json()方法返回的是obj（如果确认响应数据是json的，才可以使用json()）
    dic_obj = response.json()

    #持久化存储
    fileName=word+".json"
    fp=open(fileName,"w",encoding="utf-8")
    json.dump(dic_obj,fp,ensure_ascii=False)
    print("over!!!")
