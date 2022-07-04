# 开发者：Hei guang
# 开发时间：2022/6/30 17:11

from selenium import webdriver

driver = webdriver.PhantomJS()
url = "http://www.csdn.net/"
driver.get(url)
print(driver.current_url)
