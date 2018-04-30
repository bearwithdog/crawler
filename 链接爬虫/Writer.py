from BeautifulSoup import beautifulsoup
import csv
class writer_csv:
    def __init__(self):
        self.file=open('file.csv','a',newline='',encoding='utf-8')
        self.filelds=('用户','评论日期','评论内容')
        self.writer=csv.writer(self.file)
        self.writer.writerow(self.filelds)

    def write(self,text):
        self.writer.writerow(text)

    def writer_close(self):
        self.file.close()