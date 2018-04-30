# # import  csv
# # with open('file.csv','a',newline='') as file:
# #     filelds=('country','area')
# #     writer=csv.writer(file)
# #     writer.writerow(filelds)
# #
# #     test=[(1,2321),(2,3211)]
# #     test.append()
# #     for i in test:
# #         writer  .writerow(i)
# # import urllib.request
# # from bs4 import BeautifulSoup
# # import re
# # request=urllib.request.Request('http://www.wandoujia.com/apps/com.zl.fqbao/comment3')
# # html =urllib.request.urlopen(request).read()
# # def get_links(html):
# #     #正则表达式找到页面的所有链接
# #     soup=BeautifulSoup(html,"html.parser")
# #     if soup is not None:
# #         ul = soup.find('div', attrs={'id': 'comments'})
# #     if ul is not None:
# #         ul2 = ul.find_all('li', class_="normal-li")
# #     for urll in ul2:
# #         user=urll.find('span',attrs={'class':'name'}).get_text()
# #         content=urll.find('p',attrs={'class':'cmt-content'}).get_text()
# #         pattern=re.compile(r'[0-9]{4}年.*?日')
# #         time=pattern.search(str(urll)).group()
# #         print(user,str(time),content)
# # get_links(html)
# import  urllib.request
# import urllib.parse
# import requests
# import  re
# import json
# import request
# url='http://comment.mobilem.360.cn/comment/getComments'
# value = {}
# value['callback']='jQuery17207430712133428131_1524107886935'
# #非常重要get参数中的+号其实代表的意思是空格，所以在参数传递时不要把加号当成字符串写进去否则地址无法被解析
# value['baike']='易付宝 Android_com.suning.mobile.epa'
# value['c']='message'
# value['a']='getmessage'
# value['start']=20
# value['count']=10
# data = urllib.parse.urlencode(value)
# geturl=url+'?'+data
# print(geturl)
# #urllib.error.HTTPError: HTTP Error 403: Forbidden 这种问题原因为浏览器有防爬虫措施，所以要加头部伪装为浏览器
# headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# # req =requests.get(geturl,headers= headers)
# request=urllib.request.Request(geturl,headers=headers)
# # temp=req.text
# # regex=re.compile(r"\[.*?\]")
# # temp2=regex.search(temp)
# # html=json.loads(temp2.group())
# html=urllib.request.urlopen(request).read()
# html=html.decode('utf-8')
# regex=re.compile(r"\[.*?\]")
# temp2=regex.search(html)
# html=json.loads(temp2.group())
# # print(html)
# # html=json.dumps(html,ensure_ascii=False)
# # i=0
# # content=re.compile(r"'content':(.*?),")
# # for li in html:
# #     li=content.search((str(li)))
# #     print(li.group(1))
# # print(len(html))
print('666')