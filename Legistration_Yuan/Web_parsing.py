import requests
from bs4 import BeautifulSoup


#response = requests.get ("https://www.ly.gov.tw/Pages/List.aspx?nodeid=110")

#soup = BeautifulSoup(response.text, "html.parser")

#前面是tag name，是為了要把網頁切割，切出一個範圍來，這樣方之後針對那個範圍把東東抓出來
#後面的class_=是要透過property把東東抓出來
#section_of_interest = soup.find("section", class_="con_data")

#print(section_of_interest)

#links_of_interest = section_of_interest.find_all("a")

#f = open('LY.txt', 'w')

#for i in range(len(links_of_interest)):
#    print("",file = f)
#    print(links_of_interest[i].text, file = f)

#    extract = requests.compat.urljoin('https://www.ly.gov.tw/Pages/List.aspx?nodeid=110', links_of_interest[i]["href"])

    #open_link = requests.get(extract)
    #soup = BeautifulSoup(open_link.text, "html.parser")
    #print(extract, file = f)


#f.close


#pandas beings

#import pandas as pd


f = open("Legistration_Yuan/LY.txt", "r")

#print(f.readlines())

#read_file = pd.read_csv ('Legistration_Yuan/LY.txt')
#read_file.to_csv ('Legistration_Yuan/LY.csv', index=None)

#f = open("Legistration_Yuan/LY.csv", "a")



lines = f.readlines()
for i in range(len(lines)):
    print("RRRR")
    if i % 2 == 1:
        var = int((i+1)/2)
        f = open(f"Legistration_Yuan/LY{var}.txt", "w")
        URL = lines[i].strip("\n")
        result = requests.get(URL)
        print(result.content, file = f)    
        f.close
        
        #soup = BeautifulSoup(result.text, "html.parser")

        
        
        