#initial setup
import requests
import pandas as pd
from bs4 import BeautifulSoup

#start parsing
with open(f'PhilosL_Job/Data/WebTest.html', 'r') as f: 
    soup = BeautifulSoup(f, 'html.parser')

    # Use find_all to get all talbes rather than only the first one, which BeautifulSoup.find() does.

    #There can be multiple tables in a web page!
    tables = soup.find_all('table', class_='tableframe')
    print(f'We have {len(tables)} tables here.') #the answer is two.


#double check if every monthly archieve has exactly two tables
#this is important because if it is not the case, building a crawler will the tricky 

my_header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
    'Connection': 'keep-alive'} #this part tells the site who's visiting


response = requests.get('https://listserv.liv.ac.uk/cgi-bin/wa?A1=ind0501&L=PHILOS-L') 

sp = BeautifulSoup(response.text, 'html.parser')
check_table = soup.find_all('table', class_='tableframe')
print(f'Got {len(check_table)} tables here.') #the answer is two again. Sorted.
