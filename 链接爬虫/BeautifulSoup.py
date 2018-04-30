from bs4 import BeautifulSoup
import  re
#查找要抓取的数据返回,负责页面解析
def beautifulsoup(html,wrs):
    result=[]
    soup=BeautifulSoup(html,"html.parser")
    if soup is not None:
        ul = soup.find('div', attrs={'id': 'comments'})
    if ul is not None:
        ul2 = ul.find_all('li', class_="normal-li")
    if ul2 is not None:
        for urll in ul2:
            user=urll.find('span',attrs={'class':'name'})
            if user is not None:
                user=user.get_text()
            content=urll.find('p',attrs={'class':'cmt-content'})
            if content is not None:
                content=content.get_text()
            pattern=re.compile(r'[0-9]{4}年.*?日')
            time=pattern.search(str(urll))
            if time is not None:
                time=time.group()
                wrs.write((user, time, content))
            print(user,time,content)



def get_links(html):
        soup = BeautifulSoup(html, "html.parser")
        links = []
        if soup is not None:
            url1 = soup.find('div', attrs={'id': 'comments'})
        if url1 is not None:
            url2 = url1.find('div', attrs={'class': "page-wp roboto"})
        if url2 is not None:
            url3 = url2.find_all('a')
            for link in url3:
                links.append(link.get('href'))
        return links

