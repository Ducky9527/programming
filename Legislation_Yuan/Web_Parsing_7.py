import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

#dump personal website


#先把個人網頁的網址那個column的內容轉換成list
#for i in range(7):
#    df = pd.read_csv(f'/Users/huangpei-hua/Workspace/programming/LY_list_{i+1}.csv')
#    page_list = df['page'].tolist()


#df = pd.read_csv(f'/Users/huangpei-hua/Workspace/programming/LY_list_1.csv')
#page_list = df['page'].tolist()

#打開已經做好的csv檔
df = pd.read_csv('LY_test.csv')

#測試用page
page_list = ['https://www.ly.gov.tw/Pages/List.aspx?nodeid=1809','https://www.ly.gov.tw/Pages/List.aspx?nodeid=1810', 'https://www.ly.gov.tw/Pages/List.aspx?nodeid=1811']


education = []

#把page的網址一個一個打開
for url in page_list:
    #偽裝成Mozilla，不然的話python直接request網頁會被擋
    my_header = { 
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
        'Connection': 'keep-alive'}
    response = requests.get(url, headers = my_header)
    response.encoding ='utf-8' 
    soup = BeautifulSoup(response.text, "html.parser")

    #找出學歷欄
    list = soup.find("div", class_="col-sm-8")
    narrow = list.find("ul")
    education.append(narrow.text)

    time.sleep(3)

df['education'] = education

df.to_csv('LY_test_edu.csv', index = False)