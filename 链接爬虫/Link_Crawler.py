#链接遍历爬虫
import  re
import Download as gf
import  urllib
from Limit_Delay import limit_bandwidth
from urllib.parse import urljoin
from  Writer import writer_csv
from  BeautifulSoup import beautifulsoup
def link_carwler(seed_url,link_refex,max_depth):
    crawler=[seed_url]
    # seen=set(crawler)
    seen={seed_url:0}
    #set delay time,防止封IP,
    delay_time=limit_bandwidth(3)
    #创建要写入的CSV
    wr_csv=writer_csv()
    while crawler:
        url=crawler.pop()
        #获取下载页面的深度,防止爬虫陷阱。
        depth=seen[url]
        #check delay time
        delay_time.wait(url)
        html=gf.download(url)
        wr_csv.write(html)
        if html is not None and depth<max_depth:  #若HTML返回不为空开始进行爬取,且深度不超过最大值
            for link in get_links(html):
                #提取相对链接
                link=link.split('=')
                s=link[1][1:len(link[1])-1]
                if re.match(link_refex,s):
                    #组合为绝对链接
                    s=urljoin(seed_url,s)
                    if s not in seen: #重复链接不记录
                        #由于所有发现的链接都是在当前页面下所有新链接，所以深度都是当前页面深度+1
                        seen[s]=depth+1
                        crawler.append(s)
#通过正则表达式匹配到当前索引页所有页面链接
def get_links(html):
    #正则表达式找到页面的所有链接
    webpage_regex=re.compile(r'<a\s+href=".*?"')
    html=html.decode('utf-8')
    return webpage_regex.findall(html)
#程序入口
#set delay time
link_carwler('http://example.webscraping.com','.*/(index|view)',2)
