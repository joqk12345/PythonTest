# Created by joqk12345 on 4/3/17.
# www.github.com/joqk12345

#!/usr/bin/env python
# -*- conding:utf-8 -*-
#from urllib.request import urlopen
import urllib


class HtmlDownloader(object):

    def download(self,url):
       if url is None:
           return None

       response = urllib.urlopen(url)

       if response.getCode()!=200:
            return None
       return response.read()


