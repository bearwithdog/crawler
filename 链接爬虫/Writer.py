from BeautifulSoup import beautifulsoup
import csv
class writer_csv:
    def __init__(self):
        self.file=open('file.csv','a',newline='')
        self.filelds=('country','area')
        self.writer=csv.writer(self.file)
        self.writer.writerow(self.filelds)

    def write(self,html):
        text=beautifulsoup(html)
        self.writer.writerow(text)