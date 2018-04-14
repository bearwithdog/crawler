from bs4 import BeautifulSoup
#查找要抓取的数据返回
def beautifulsoup(html):
    soup=BeautifulSoup(html,"html.parser")
    if soup is not  None:
        ul = soup.find('tr', attrs={'id': 'places_area__row'})
        ull=soup.find('tr',attrs={'id':"places_country__row"})
    if ul is not  None:
        ul2 = ul.find('td', class_="w2p_fw")
        area=ul2.text
    else:
        area=None
    if ull is not None:
        ull2=ull.find('td',attrs={'class':'w2p_fw'})
        country=ull2.text
    else:
        country=None
    return (country,area)

