#-*- coding:UTF-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from testproxy.items import *
import re


class Doctor(Spider):
    name = "doctor"
    start_urls = ['http://400.haodf.com/']
    allow_domaim = ['haodf.com']
    # custom_settings = {                  #关闭pipeline
    #     'ITEM_PIPELINES' : {
    #         # 'yuanyuan.pipelines.*****Pipeline': 300
    #     }
    # }
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    #
    # }
    # #
    # def make_requests_from_url(self, url):
    #     return Request(url=url, headers=self.headers)


    def parse(self, response): #获取科室的urls
        print response.body
        # sel = Selector(response)
    #     ks_urls = sel.xpath('//a[@class="black_link"]/@href').extract()
    #     for url in ks_urls:
    #         url = "http://haoping.haodf.com" + str(url).strip(".htm") + "/daifu.htm"
    #         # print url
    #     # print(len(ks_urls))
    #         yield Request(url=url, callback= self.get_doc_url )
    #
    # def get_doc_url(self, response):#获取医生的urls
    #     sel = Selector(response)
    #     doc_urls = sel.xpath('//ul[@class="yy_jb_df"]/li/a[@class="blue"]/@href').extract()
    #     # pages_temp = sel.xpath('//a[@class="p_text"][1]/text()').extract()[0]
    #     for url in doc_urls:
    #         print url
    #
    #     # mode = re.compile(r'\d+')
    #     # last_page = mode.findall(pages_temp)[0]
    #     # if last_page > 1:
    #     #     for page in range(1,last_page):
    #     #
    #     #
    #     # else:
    #     #     pass






