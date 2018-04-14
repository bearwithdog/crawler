import Download as gf
import urllib.request
import  time
import itertools
#ID遍历爬虫
def crawl_sitemap():
    for page in itertools.count(1):
        print(page)
        time.sleep(0)
        url='http://example.webscraping.com/places/default/view/'+str(page)
        html=gf.download(url)
        if html is not None:
            pass
        else:
            break

crawl_sitemap()

