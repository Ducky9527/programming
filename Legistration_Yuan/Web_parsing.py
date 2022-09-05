import requests
from bs4 import BeautifulSoup


response = requests.get ("https://www.ly.gov.tw/Pages/List.aspx?nodeid=110")

soup = BeautifulSoup(response.text, "html.parser")

#前面是tag name，是為了要把網頁切割，切出一個範圍來，這樣方之後針對那個範圍把東東抓出來
#後面的class_=是要透過property把東東抓出來
section_of_interest = soup.find("section", class_="con_data")

#print(section_of_interest)

links_of_interest = section_of_interest.find_all("a")

f = open('LY.txt', 'w')

for i in range(len(links_of_interest)):
    print("",file = f)
    print(links_of_interest[i].text, file = f)
    extract = requests.compat.urljoin('https://www.ly.gov.tw/Pages/List.aspx?nodeid=110', links_of_interest[i]["href"])
    print(extract, file = f)

print("meow"*i)

for i in range(9):
    print("meow"*i)

print("meow"*i)

#for link in links_of_interest:
#    print("",file = f)
#    print(link.text, file = f)
#    extract = requests.compat.urljoin('https://www.ly.gov.tw/Pages/List.aspx?nodeid=110', link["href"])
#    print(extract, file = f)

f.close