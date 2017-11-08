# Test Program to parse and convert HTML data

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://qiita.com/ay3/items/8d758ebde41d256a32dc')
soup = BeautifulSoup(html, "lxml")

art = soup.find("article")

title = art.find("div", {"class":"ArticleMainHeader"}).h1
print("Title : " + title.text)
 
for sub in art.find("div", {"id":"article-body-wrapper"}).findAll({"h1","h2", "h3"}):
    print("Chapter : " + sub.text)



