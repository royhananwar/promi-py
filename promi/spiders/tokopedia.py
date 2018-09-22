# -*- coding: utf-8 -*-
import scrapy
import json

class TokopediaSpider(scrapy.Spider):
    name = 'tokopedia'
    allowed_domains = ['tokopedia.com']
    start_urls = ['https://tokopedia.com/promo/']

    def parse(self, response):
        print("---------------------------------------------------------------------------------")
        print("                 Start Crawl")
        print("---------------------------------------------------------------------------------")
        print("result", response.body)
        pass
