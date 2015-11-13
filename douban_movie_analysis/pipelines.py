# -*- coding: utf-8 -*-
#encoding:utf-8

import pymongo
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanMovieAnalysisPipeline(object):
    def __init__(self):
        self.mongo_url='localhost'
        self.mongo_port=27017
        self.collection_name='analysis'
        self.db_name='douban_analysis'

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_url,self.mongo_port)
        self.db=self.client[self.db_name]
        self.con=self.db[self.collection_name]

    def close_spider(self,spider):
            self.client.close()

    def process_item(self, item, spider):
        for i in item['analysis']:
            if self.con.find_one({"analysis":unicode(i)}): # 在数据库中查找是否已存在该类型，存在则将‘count’项+1
                add_one=self.con.find_one({'analysis':str(i)})
                print add_one
                count=int(add_one['count'])
                count=count+1
                add_one['count']=count
                print add_one
                print count
                self.con.save(add_one)
            else: # 若不存在则新建该项
                self.con.insert_one({'analysis':i,"count":1})
                print "hello"
        print item['analysis']