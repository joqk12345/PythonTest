#!/usr/bin/env python
# -*- conding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors
#获取数据库链接
connection = pymysql.connect(host='localhost',user='root',password='123456',db='urls',charset='utf8')
try:
    with connection.cursor() as cursor:
                # 创建sql语句
         sql="select `urlname`,`urlhref` from urls WHERE  `id` is not NULL "
         #执行sql语句
         count = cursor.execute(sql)
         print(count)

         result = cursor.fetchmany(size=3)
         print(result)
finally:
     connection.close()