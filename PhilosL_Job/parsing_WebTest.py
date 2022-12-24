#initial setup
import requests
import pandas as pd
from bs4 import BeautifulSoup



#start parsing



with open(f'PhilosL_Job/Data/WebTest.txt', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

    table = soup.find('table', class_='tableframe')

    data = []

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    print(data)
    
    #for row in table.find_all('tr')
    #    cells = row.find_all('td')
    #text = table.find_all('a')

    #for i in range(len(text)):
    #    print(text[i]['href'])
    #    print(text[i].text)