# -*- coding: utf-8 -*-
import scrapy
import datetime
from moly_scraper.items import moly_items

class MolySpider(scrapy.Spider):
    name = "moly"
    allowed_domains = ["moly"]
    start_urls = ["https://moly.hu/konyvek"]

    def parse(self, response):
        #g = 0
        #item = moly_items()
        for t, r in zip(response.xpath("//h3/a/text()").getall(), response.xpath("//h3/span[1]/text()").getall()):
            yield moly_items(title = t, rating = r)
        
#        for r in response.xpath("//h3/span[1]/text()").getall():
#            yield moly_items(rating = r)
            

        #with open("moly_konyvek.txt", "a") as f:
        #    f.write(t + "\n")
