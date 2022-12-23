#把網頁整個抓下來存成txt檔
import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.ly.gov.tw/Pages/List.aspx?nodeid=37103")

soup = BeautifulSoup(response.text, "html.parser")
list = soup.find("section", class_="con_data")
name = list.find_all("a")


f = open('LY1_1.txt', 'w')

for i in range(len(name)):
    print("", file=f)
    print(name[i].text, file=f)

    extract = requests.compat.urljoin(
        'https://www.ly.gov.tw/Pages/List.aspx?nodeid=37103', name[i]["href"])

    open_link = requests.get(extract)
    soup = BeautifulSoup(open_link.text, "html.parser")
    print(extract, file=f)

    print(name[i]["href"])

f.close()
