#!/usr/bin/env python
# -*- conding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#请求url并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Wiki").read().decode("utf-8")
#使用beautifulsoup去解析
soup = BeautifulSoup(resp,"html.parser")
#获取所有以/wiki 开头的a标签的href属性
listUrls =soup.find_all("a",href=re.compile("^/wiki/"))
for url in listUrls:
    if not re.search("\.(jpg|JPG)$",url["href"]):
        #输出URL的文字和对应的链接
        # string只能获取一个 get_text() 获取标签下的所有文字
        print(url.get_text(),"<----->","https://en.wikipedia.org/"+url["href"])