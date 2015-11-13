import  matplotlib.pyplot as plt
x=[1,2,3,4]
y=[5,4,3,2]
plt.figure()
plt.subplot(231)
plt.plot(x,y)
plt.subplot(232)
plt.bar(x,y)
plt.subplot(233)
plt.barh(x,y)
plt.subplot(234)
plt.bar(x,y)
y1=[7,8,5,3]
plt.bar(x,y1,bottom=y,color='r')
plt.subplot(235)
plt.boxplot(x)
#绘制盒图
plt.subplot(236)
plt.scatter(x,y)
plt.show()


'''
参考资料：
1.Python数据可视化编程实战
2.http://www.blogjava.net/norvid/articles/317235.html  关于盒图的介绍。
'''
