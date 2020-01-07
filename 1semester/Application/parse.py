from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right")
bsObject = BeautifulSoup(html,"html.parser")

table = bsObject.find("table")
titles = table.find_all(class_="title")
for title in titles:
    x=title.get_text()
    x=x.replace("\t",'')
    x=x.replace("\n",'')
    x=x.strip()
    link = title.a.get('href')
    url = 'http://www.hufs.ac.kr/user/' + link
    print(x)
    print(url)


