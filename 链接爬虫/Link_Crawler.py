#链接遍历爬虫
import  re
import Download as gf
import  urllib
from Limit_Delay import limit_bandwidth
from urllib.parse import urljoin
from  Writer import writer_csv
from  BeautifulSoup import get_links
from  BeautifulSoup import beautifulsoup
def link_carwler(seed_url,wr_csv,max_depth):
    crawler=[seed_url]
    # seen=set(crawler)
    seen={seed_url:0}
    #set delay time,防止封IP,
    delay_time=limit_bandwidth(3)
    #创建要写入的CSV

    while crawler:
        url=crawler.pop()
        #获取下载页面的深度,防止爬虫陷阱。
        depth=seen[url]
        #check delay time
        delay_time.wait(url)
        html=gf.download(url)
        #写入爬取的数据
        if html is not  None:
            beautifulsoup(html, wr_csv)
        if html is not None and depth<max_depth:  #若HTML返回不为空开始进行爬取,且深度不超过最大值
            for link in get_links(html):
                if link not in seen: #重复链接不记录
                    #由于所有发现的链接都是在当前页面下所有新链接，所以深度都是当前页面深度+1
                    seen[link]=depth+1
                    crawler.append(link)

#程序入口
wr_csv=writer_csv()
link_carwler('http://www.wandoujia.com/apps/com.msxf.loan/comment2',wr_csv,100)
wr_csv.writer_close()