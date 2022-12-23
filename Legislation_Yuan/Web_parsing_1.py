#將立法院的存放歷屆立法委員的名單的網址一個一個抓下來，方便之後把所有的名單資訊存下來

#匯入可以自動request網頁資訊的東東們
import requests
#匯入可以把網頁資訊整理成人能看的、程式可以找東東的樣子的漂亮湯
from bs4 import BeautifulSoup


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
f = open('Legislation_Yuan/Data/URL.txt', 'w' )

#先看一下list裡面抓出來的東西是怎麼存的，確認出list中的東東都是「連結＋文字檔」，看完記得就刪掉
#print(len(list))

#利用for迴圈把list中的東東一個一個print出來到指定的檔案file = f 中
for i in range(len(list)):
    print(list[i].text, file=f)
    print(list[i],file=f)


 