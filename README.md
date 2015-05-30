水木爬虫
===========

一个基于scrapy的爬虫, 提取水木上不同版块帖子的url, 标题, 发帖时间以及作者

默认爬取30页, 输出结果为一个json文件(版块名_时间.json)

###使用方法
例如, 要下载房地产论坛的帖子

在有scrapy.cfg文件的目录下执行

```
scrapy crawl board -a board=RealEstate
```

###防ban策略
+ 随机下载时间
+ 禁止cookie
+ 随机采用UserAgent