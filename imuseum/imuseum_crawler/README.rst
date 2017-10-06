IMuseum  爬虫
===========================


## Design

爬虫参考了 Scrapy, 数据流与控制流分离。使用了 asyncio 异步非阻塞的IO 库。


### Components

各部件的行为参考 https://docs.scrapy.org/en/latest/topics/architecture.html

 - engine
 - scheduler
 - spider
 - pipeline



## 爬虫分析

参考 `parser.rst`

