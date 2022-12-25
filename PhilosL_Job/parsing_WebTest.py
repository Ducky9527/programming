#initial setup
import requests
import pandas as pd
from bs4 import BeautifulSoup

#start parsing
with open(f'PhilosL_Job/Data/WebTest.html', 'r') as f: # 窩偏要用html
    soup = BeautifulSoup(f, 'html.parser')

    # Use find_all to get all talbes rather than only the first one, which BeautifulSoup.find() does.
    tables = soup.find_all('table', class_='tableframe')
    print(f'We have {len(tables)} tables here.')
    data = []

    # We dont't want the first table. It's merely the table of content.
    table = tables[1]
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    for row in data:
        print(row)
    
    #for row in table.find_all('tr')
    #    cells = row.find_all('td')
    #text = table.find_all('a')

    #for i in range(len(text)):
    #    print(text[i]['href'])
    #    print(text[i].text)