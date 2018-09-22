# -*- coding: utf-8 -*-
import scrapy


class BukalapakSpider(scrapy.Spider):
    name = 'bukalapak'
    allowed_domains = ['bukalapak.com']
    start_urls = ['https://bukalapak.com/promo']

    def parse(self, response):
        print("---------------------------------------------------------------------------------")
        print("                 Start Crawl")
        print("---------------------------------------------------------------------------------")
        print("result", response.body)