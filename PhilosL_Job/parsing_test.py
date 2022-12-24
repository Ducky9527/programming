#initial setup
import requests
from bs4 import BeautifulSoup

my_header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
    'Connection': 'keep-alive'}



#start parsing
response = requests.get('https://listserv.liv.ac.uk/cgi-bin/wa?A1=ind2212&L=PHILOS-L',
headers = my_header)

soup = BeautifulSoup(response.text, 'html.parser')

#title = soup.find('table', class_='emphasizedgroup')
#title_extract = soup.find_all('h2')
#print(title_extract)
extract = soup.find('table', class_='tableframe')
text = extract.find_all('a')

for i in range(len(text)):
    print(text[i]['href'])
    print(text[i].text)
    
