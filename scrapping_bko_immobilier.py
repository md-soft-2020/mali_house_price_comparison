from bs4 import BeautifulSoup
import requests


url1 = "https://www.bamako-immobilier.com/741-location-appartements-bamako.html"
url2 = "https://www.bamako-immobilier.com/1711-location-appartements-kalaban-koura--kalaban-koura.html"
url3 = "https://www.bamako-immobilier.com/2860-location-appartements-faso-kanu.html"

page1 = requests.get(url1)
# page2 = requests.get(url2)
# page3 = requests.get(url3)

soup1 = BeautifulSoup(page1.text, "html.parser")
# soup2 = BeautifulSoup(page2.text, "html.parser")
# soup3 = BeautifulSoup(page3.text, "html.parser")

# urls = [url1, url2, url3]
# pages = [page1, page2, page3]
# soups = [soup1, soup2, soup3]

# grab annonce title
init = soup1.find(class_= "zonegris mt2")
t = init.h2 # this simular to p = init.find("h2")
a_title = [x.get_text() for x in t][1]

# # grab more infos about annonce
# m_info = init.find(class_= "row grid2")
# # k = [t.get_text(strip= True) for t in m_info]
# for i in m_info:
#     print((i.find("br")).get_text)

# annonce description
annonce = init.find(class_= "row mt1")
desc = [x.get_text(strip= True) for x in annonce]
for i in desc:
    if len(i) > 10:
        a_desc = i

# Full infos about the annonce
full_infos = {
    "title" : a_title,
    "description": a_desc
}

print(full_infos["title"])