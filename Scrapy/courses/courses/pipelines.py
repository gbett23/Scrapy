# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import json

#class CoursesPipeline(object):

	#def __init__(self):
		#self.file = open('items.jl', 'wb')

    #def process_item(self, item, spider):
    	#line = json.dumps(dict(item)) + "\n"
    	#self.file.write(line)

    	#return item

#from scrapy import signals
#from scrapy.exporters import XmlItemExporter

#class XmlExporterPipeline(object):

#	def __init__(self):
#		self.files = {}

#	@classmethod
#	def from_crawlers(cls, crawler):
#		pipeline = cls()
#		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#		crawler.signals.conncet(pipeline.spider_closed, signals.spider_closed)
#		return pipeline

#	def spider_opened(self, spider):
#		file = open('%s_products.xml' % spider.name, 'w+b')
#		self.files[spider] = fileself.exporter = XmlItemExporter(file)
#		self.exporter.start_exporting()

#	def spider_closed(self, spider):
#		self.exporter.finish_exporting()
#		file = self.files.pop(spider)
#		file.close()

#	def process_item(self, item, spider):
#		self.exporter.export_item(item)
#		return item