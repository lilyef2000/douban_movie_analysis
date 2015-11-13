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
        
        # Description:��ȡӰƬ����
        # 
        # Input:ץȡ��ӰƬ�����ַ���
        #
        # Output:ȷ�ϵ�ӰƬ����
        x=[]
        for i in analysis:
            if len(i)>5 and ':' not in i: #
                i=i.split('/') # �ַ����á�/���ֿ��γ��ַ�������
                i=i[-1]  # ȡ�������һ���ַ���i=i[len(i)-1]

                i=i.strip() # ȥ���ַ�����ǰ�����Ŀո�
                i=i.replace(" ","") #ȥ���ַ����м�Ŀո�
                word=unicode(i) # ���ַ���ת��unicode����

                if word!=" " and len(word)>0:

                    print len(word)
                    print word

                    words=jieba.cut(word,cut_all=False) # ���ַ����ֳ����Ĵ���
                    for n in words:
                        print n
                        x.append(n) # ���д��x�б�

        item['analysis']=x        
        yield item
