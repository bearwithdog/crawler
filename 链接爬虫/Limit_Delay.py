#限制下载速度的类
import  datetime
from urllib.parse import urlparse
import time
class limit_bandwidth:
    def __init__(self,delay):
        #delay设置延迟时间
       self.delay=delay
        #字典项，键名为url，键值是上次下载时间
       self.domin={}

    def wait(self,url):
        dom=urlparse(url).netloc
        last_accessed=self.domin.get(dom)
        if self.delay>0 and last_accessed is not None:
           sleep_time=self.delay-(datetime.datetime.now()-last_accessed).seconds
           if sleep_time>0:
               time.sleep(sleep_time)
        self.domin[dom]=datetime.datetime.now()




