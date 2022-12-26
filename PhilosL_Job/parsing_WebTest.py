#initial setup
import requests
import pandas as pd
from bs4 import BeautifulSoup

#start parsing
with open(f'PhilosL_Job/Data/WebTest.html', 'r') as f: 
    soup = BeautifulSoup(f, 'html.parser')

    # Use find_all to get all talbes rather than only the first one, which BeautifulSoup.find() does.
    tables = soup.find_all('table', class_='tableframe')
    print(f'We have {len(tables)} tables here.')
    


    data = [] #create an empty variable first, so that we can store values in it later.


    # We dont't want the first table. It's merely the table of content. It doesn't have URLs and other information. 

    table = tables[1] #Remember, the numbering begins with 0. So the second table is table [1]

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    for row in data:
        print(row)
    