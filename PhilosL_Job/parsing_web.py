#initial setup
import requests
from bs4 import BeautifulSoup

my_header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
    'Connection': 'keep-alive'}

#start parsing
response = requests.get('https://listserv.liv.ac.uk/cgi-bin/wa?A0=PHILOS-L',
headers = my_header)

soup = BeautifulSoup(response.text, 'html.parser')

#locating the URLs
archieve_list = soup.find(class_='normalgroup')


#f = open('PhilosL_Job/Data/URL_List.txt', 'w')

for a in archieve_list.find_all('a', href=True):
    open_list = 'https://listserv.liv.ac.uk/'+ a['href']

    response = requests.get('open_list')

        sp = BeautifulSoup(response.text, 'html.parser')
        extract = soup.find('table', class_='tableframe')
        text = extract.find_all('a')

        for i in range(len(text)):
            print(text[i].text)
            print(text[i]['href'])

    #if wish to save to a separate file, then
    #print('https://listserv.liv.ac.uk/'+ a['href'], file = f)







    
