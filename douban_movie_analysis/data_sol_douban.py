# -*- coding: utf-8 -*-
#encoding:utf-8

import matplotlib.pyplot as plt
from pylab import *

import pymongo  
from matplotlib.font_manager import FontProperties
import subprocess
import numpy as np

font=FontProperties(fname=r'C:\WINDOWS\Fonts\MSYH.ttf',size=10)

def pic_show():
    client=pymongo.MongoClient("localhost",27017)

    db=client['douban_analysis']

    con=db['analysis']

    data=[]
    analysis=[]

    for item in con.find():
        data.append(item['count'])
        analysis.append(item['analysis'])

    print data
    for n in  analysis:
        print n

    y_pos=range(len(analysis))

    colors = np.random.rand(len(analysis))

    plt.barh(y_pos,data,align='center',alpha=0.4)
    plt.yticks(y_pos,analysis,fontproperties=font)
    for data,y_pos in zip(data,y_pos):
        plt.text(data,y_pos,data,horizontalalignment='center',verticalalignment='center', weight='bold')
    plt.ylim(+28.0,-1.0)
    plt,title(u"豆瓣电影top250 分类统计",fontproperties=font)
    plt.ylabel(u"电影分类",fontproperties=font)
    plt.subplots_adjust(bottom = 0.15)
    plt.xlabel(u"分类出现次数（一部影片分类可以多个）",fontproperties=font)
    plt.savefig("douban_analysis_new.png")  

pic_show()