import urllib.request
import  time
import itertools
# 重试次数num_retrise
def download(url,user_agent='wswp',num_retrise=2):
    while num_retrise>0 :
        print ('Downloading:',url)
        headers={'User-agent':user_agent}
        request=urllib.request.Request(url,headers=headers)
        try:
            html=urllib.request.urlopen(request).read()
            break;
        except urllib.error.URLError as e:
            print('Downloading Error',e.reason,e.code)
            html=None
            num_retrise-=1
            if hasattr(e,'code') and 500<=e.code<600:
                continue
            else:
                break
    return html
