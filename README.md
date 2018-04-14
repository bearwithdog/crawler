# crawler
# 一、ID遍历爬虫，爬虫入门：利用网页的ID索引遍历下载所有网页，但是遇到网页ID不连续时无法下载。通过这个可以了解爬虫的工作原理。
# 二、链接爬虫
## 各文件功能：
BeautifulSoup.py<br>
提取HTML中需要的信息，利用python的beautifulsoup，不得不说比正则表达式爽太多。<br>
Download.py<br>
打开网页，读取网页内容。<br>
Limit_Delay.py<br>
设置相同网页的下载延迟，避免下载速度过快导致IP禁用，默认3秒<br>
Link_Crawler.py<br>
链接爬虫各模块的主调度程序，程序主入口<br>
Writer.py<br>
将提取出的内容写入到CSV中<br>
测试.py<br>
没用的文件，主要用来测试API的使用方法<br>
## 总结：
目前的链接爬虫工作原理为，读取根链接，打开该网页提取所有url，存进队列中，逐个打开url读取网页内容同时再提取出url存进队列中，<br>
实现了网页链接爬取。<br>
## 特点：
1、下载速度可以调<br>
2、可以调节爬取深度，防止落入爬虫陷阱<br>
## 下一步规划：
爬虫缓存，分布式爬虫。<br>
本次demo爬取了 http://example.webscraping.com/ 网站中所有国家的名称已经面积。file.csv记录不全是因为默认的爬取深度为2，所以只会递进两层。
