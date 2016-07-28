# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from courses.items import CoursesItem
#from courses.pipelines import CoursesPipeline

class CoursesSpider(scrapy.Spider):
    name = "Courses"
    allowed_domains = ["www.swingbyswing.com"]
    start_urls = [
        "https://www.swingbyswing.com/courses/United-States/TX/New-Braunfels/Bandit-Golf-Club/25094",
        #/United-States/TX/New-Braunfels/Bandit-Golf-Club/25094
        #"https://www.swingbyswing.com/courses/United-States/TX/Austin/Great-Hills-Golf-Course/21495",
    ]

    #rules = [Rule(LinkExtractor(), callback="parse", follow=True),]

    #def parse(self, response):

        #for url in response.css("ul li a::attr('href')"):

            #url = response.urljoin(href.extract())
            #yield scrapy.Request(response.urljoin(url), self.parse_dir_contents)

    def parse(self, response):
        item = CoursesItem()
        #address container path - //section[@class="address-map-container"]/div[@class="address-map"]/address[@itemprop="address"]       	
        	
        item['course'] = response.xpath('//div[@class="col-xs-12 m-t-3 m-b-0 p-b-0"]/span[@itemprop="name"]/text()').extract()
        item['address'] = response.xpath('.//a/span[@itemprop="streetAddress"]/text()').extract()
        item['city'] = response.xpath('.//a/span[@itemprop="addressLocality"]/text()').extract()
        item['state'] = response.xpath('.//a/span[@itemprop="addressRegion"]/text()').extract()
        item['phone_number'] = response.xpath('//*[@id="content"]/div/div/div[4]/div[2]/div[1]/div[2]/section/div/address/text()').extract()

        rows = response.xpath('//tr/td/text()').extract()
        for row in rows:
            print row

        yield item