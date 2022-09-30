#將立法院的存放歷屆立法委員的名單的網址一個一個抓下來，方便之後把所有的名單資訊存下來

#匯入可以自動request網頁資訊的東東們
import requests
#匯入可以把網頁資訊整理成人能看的、程式可以找東東的樣子的漂亮湯
from bs4 import BeautifulSoup

#匯入可以弄出csv的動物
import pandas as pd

#匯入可以叫程式睡一下覺然後再執行一次的功能
import time
#匯入可以處理regular expression的東東
import re

#宣示一下等等要用什麼身份造訪網頁
my_header = { 
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
    'Connection': 'keep-alive'}

#request網頁資訊，記得要跟人家說自己是什麼身份
response = requests.get('https://www.ly.gov.tw/Pages/List.aspx?nodeid=110', headers = my_header)

#因為網頁用到utf-8的編碼，所以要邊一下不然會亂碼
response.encoding ='utf-8' 

#用漂亮湯還他漂漂
soup = BeautifulSoup(response.text,'html.parser')

#到這邊後可以先print一下，看一下資料長相
#print(soup)

#使用觀察法（chrome: View->developer->developer tools，按下去之後跳出的分割視窗，找到最左上角的那個小鼠標按下去，在原本的網頁滑來滑去時就可以看到每個東東是放在html的哪邊），發現歷屆立委名單的網頁都是存在“section"下面，所以先用這樣把要搜尋的部分限縮起來
search_list = soup.find('section', class_='con_data')
list = search_list.find_all('a')

#開一個檔案準備把抓出來的資料寫進去
#f = open('Legislation_Yuan/Data/URL.txt', 'w' )

#先看一下list裡面抓出來的東西是怎麼存的，確認出list中的東東都是「連結＋文字檔」
#print(len(list))

#利用for迴圈list中的東東一個一個加進url這個清單中
url = []
for i in range(len(list)):
#    print(list[i].text, file=f)
    temp_url = 'https://www.ly.gov.tw'+list[i]["href"]
    url.append(temp_url)

#注意！！！不可以值接寫成下面這樣
#   url.append('https://www.ly.gov.tw'+list[i]["href"])
#因為append()只處理read only的東西，他不能處理可以被修改的東西
#因此，要使用append把網址加進去，要先用一個temp_url暫時性的將網址存進這個變數，然後再讓append去讀取、存放    


#一個link一個link打開來，再用一次漂亮湯把網頁上我們有興趣的的資料抓下來
i = 10
for link in url:
    i -= 1

    my_header = { 
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
        'Connection': 'keep-alive'}
    response = requests.get(link, headers = my_header)
    response.encoding ='utf-8' 
    soup = BeautifulSoup(response.text, "html.parser")

    sections = soup.find_all("section")

    for section in sections:
        if "id" in section:
            break

    legislators = section.find_all("div", {"class": "inner"})
    legislators_df = pd.DataFrame(columns = ['name', 'party', 'url'])
    personal_page = []




    for legislator in legislators:
        name = legislator.find("div", {"class": "legislatorname"}).text
        name = re.sub(r"[\n\t\s]*", "", name)
        personal_page_path = 'https://www.ly.gov.tw' + legislator.find("a")["href"]
        party = legislator.find("img")["alt"].rstrip("徽章")
        legislators_df.loc[len(legislators_df.index)] = [name, party, personal_page_path]
        personal_page.append(personal_page_path)
    
    education = []

    for pg in personal_page:
        my_header = { 
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
        'Connection': 'keep-alive'}
        response = requests.get(pg, headers = my_header)
        response.encoding ='utf-8' 
        soup = BeautifulSoup(response.text, "html.parser")
        list = soup.find("div", class_="col-sm-8")
        narrow = list.find("ul")
        education.append(narrow.text)
        
    
    legislators_df['education'] = education
    legislators_df = legislators_df.rename(columns={'personal_page_path' : 'url'})
    legislators_df = legislators_df[['name', 'party', 'education', 'url']]

    
    legislators_df.to_csv(f"Legislation_Yuan/Data/LY_list_education_{i}.csv", index = False)
    time.sleep(1)

    

   
