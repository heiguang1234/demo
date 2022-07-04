# 开发者：Hei guang
# 开发时间：2022/6/30 21:58
import urllib.request

# 下载网页
url_page = "http://www.baidu.com"
urllib.request.urlretrieve(url_page, "baidu.html")
# 下载图片
url_image = "https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=lisa&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=1936779164,2145981191&os=651923772,1604357066&simid=1936779164,2145981191&pn=2&rn=1&di=7108135681917976577&ln=1408&fr=&fmq=1656598526768_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fc-ssl.duitang.com%252Fuploads%252Fblog%252F202107%252F09%252F20210709223137_89dd0.thumb.1000_0.jpg%26refer%3Dhttp%253A%252F%252Fc-ssl.duitang.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1659190526%26t%3Db2154514313ae8dbd312a962f3ad0d37&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwzLDEsNiw0LDUsNyw4LDIsOQ%3D%3D"
urllib.request.urlretrieve(url_image, "lisa.png")
# 下载视频
url_video = "https://vd4.bdstatic.com/mda-nfvag8ycj2rjcg5c/sc/cae_h264/1656576273188045559/mda-nfvag8ycj2rjcg5c.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1656599936-0-0-5fa21b8a60e24ef09ca9ec55f58ec3fd&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=0536673415&vid=8221302729859323115&abtest=102836_2-102976_1-102982_2-103166_4&klogid=0536673415"

urllib.request.urlretrieve(url_video, "guimie.mp4")
