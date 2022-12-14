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


#save the parsed web for future testing
#the benefit of doing this is that we will not keep disturbing the site while we do something stupid

f = open('PhilosL_Job/Data/WebTest.txt', 'w')
print(soup, file = f)    
