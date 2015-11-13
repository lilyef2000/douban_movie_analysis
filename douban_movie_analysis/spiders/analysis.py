# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
import jieba

from douban_movie_analysis.items import DoubanMovieAnalysisItem


class AnalysisSpider(CrawlSpider):
    name = 'analysis'
    allowed_domains = [] #'www.movie.douban.com'
    # download_delay = 1
    start_urls = ['http://movie.douban.com/top250?start=0&filter=&type=']

    rules = (
        Rule(LinkExtractor(allow=r'http://movie\.douban\.com/top250\?start=\d+\&filter=\&type='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #i = DoubanMovieAnalysisItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i

        sel=Selector(response)
        item=DoubanMovieAnalysisItem()
        analysis=sel.xpath("//div[@class='info']/div[@class='bd']/p/text()").extract()

        print type(analysis)
        
        # Description:截取影片类型
        # 
        # Input:抓取的影片类型字符段
        #
        # Output:确认的影片类型
        x=[]
        for i in analysis:
            if len(i)>5 and ':' not in i: #
                i=i.split('/') # 字符串用‘/’分开形成字符串数组
                i=i[-1]  # 取数组最后一个字符串i=i[len(i)-1]

                i=i.strip() # 去掉字符串最前和最后的空格
                i=i.replace(" ","") #去掉字符串中间的空格
                word=unicode(i) # 将字符串转成unicode编码

                if word!=" " and len(word)>0:

                    print len(word)
                    print word

                    words=jieba.cut(word,cut_all=False) # 把字符串分成中文词语
                    for n in words:
                        print n
                        x.append(n) # 结果写进x列表

        item['analysis']=x        
        yield item
