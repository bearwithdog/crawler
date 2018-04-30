#使用get方法获取
#用来抓取json返回的数据
import  re
import json
import urllib.parse
import  urllib.request
from    Writer import writer_csv
def write(text):
    for line in text:
        user_name=line['username']
        content=line['content']
        creat_time=line['create_time']
        print(user_name,content,creat_time)
        text=(user_name,creat_time,content)
        writer.write(text)

#非常重要get参数中的+号其实代表的意思是空格，所以在参数传递时不要把加号当成字符串写进去否则地址无法被解析
url='http://comment.mobilem.360.cn/comment/getComments'
value = {}
value['callback']='jQuery172009747548981384813_1524398091429'
value['baike']='51账单 51zhangdan Android_com.zhangdan.app'
value['c']='message'
value['a']='getmessage'
value['start']=0
value['count']=10
#将提交的参数转码为浏览器接受的格式，+号其实代表的意思是空格，所以在参数传递时不要把加号当成字符串写进去否则地址无法被解析
data = urllib.parse.urlencode(value)
geturl=url+'?'+data
print(geturl)
#urllib.error.HTTPError: HTTP Error 403: Forbidden 这种问题原因为浏览器有防爬虫措施，所以要加头部伪装为浏览器
#爬虫过程报错：http.client.RemoteDisconnected: Remote end closed connection without response
#利用 urllib 发起的请求，UA 默认是 Python-urllib/3.5 而在 chrome 中访问 UA 则是 User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36，因为服务器根据 UA 来判断拒绝了 python 爬虫。伪装为谷歌浏览器就可以顺利完成
# headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

request=urllib.request.Request(geturl,headers=headers)
html=urllib.request.urlopen(request).read()
html=html.decode('utf-8')
regex_content=re.compile(r"\[.*?\]")
text=regex_content.search(html).group()
# text=json.loads(text)
regex_total=re.compile(r'"total":(.*?),')
total=regex_total.search(html).group(1)
writer=writer_csv()
while value['start']<int(total):
    value['start'] = value['start']+10
    data = urllib.parse.urlencode(value)
    geturl = url + '?' + data
    request = urllib.request.Request(geturl, headers=headers)
    html = urllib.request.urlopen(request).read()
    html = html.decode('utf-8')
    text = regex_content.search(html).group()
    text = json.loads(text)
    write(text)
writer.writer_close()



