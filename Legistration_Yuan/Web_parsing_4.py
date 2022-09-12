import requests
from bs4 import BeautifulSoup




for i in range(7):
    
    f = open(f'LY_list_{i+1}.txt', 'w')
    with open(f"Legistration_Yuan/LY{i+1}.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        list = soup.find("section", class_="con_data")
        name = list.find_all("a")

        for j in range(len(name)):
            
            print(name[j].text, file=f)
            print(name[j]["href"], file = f)