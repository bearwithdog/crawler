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
            return html
        except urllib.error.URLError as e:
            print('Downloading Error',e.reason)
            html=None
        if num_retrise>0:
            num_retrise-=1
            continue
        else:
            break
    return html
