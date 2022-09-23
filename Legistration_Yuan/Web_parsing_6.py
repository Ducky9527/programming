#把只有片段的網址變成完整的網址

from bs4 import BeautifulSoup
import pandas as pd


#匯入檔案
for i in range(7):
    df = pd.read_csv(f'/Users/huangpei-hua/Workspace/programming/LY_list_{i+1}.csv')

    #新增一個內容全部都是 https://www.ly.gov.tw 的column
    whole_url = 'https://www.ly.gov.tw'
    df['Whole_Url'] = whole_url

    #把這個column的內容跟先前的網址片段黏起來
    df['page'] = df['Whole_Url'] + df['url']

    #更新輸出的內容
    df = df[["name", "party", 'page']]

    df.to_csv(f"/Users/huangpei-hua/Workspace/programming/LY_List_{i+1}.csv", index = False)


