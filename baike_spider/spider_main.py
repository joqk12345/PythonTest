# Created by joqk12345 on 4/3/17.
# www.github.com/joqk12345

#!/usr/bin/env python
# -*- conding:utf-8 -*-
#from baike_spider import url_manager,html_downloader,html_parser,html_outputer
import baike_spider.html_downloader
import baike_spider.url_manager
import baike_spider.html_parser
import baike_spider.html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer =html_outputer.HtmlOutputer()

    def craw(self,roo_url):
        count =1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d:%s' % count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_date = self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_date)
                if count ==1000:
                    break
            except:
                print ('craw failed')

        self.outputer.output_html()

if __name__ == '__main__':
    root_url ="http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
