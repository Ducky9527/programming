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


#Get the URLs

####option 1 - only print out the URLs
for a in archieve_list.find_all('a', href=True):
    print('https://listserv.liv.ac.uk/'+ a['href'])



###option 2 - print out the URLs and save them in a separate txt file so that we will not need to visit the website to get the URLs when we want to use them to do stuff next time. 

#open a new file in the designited location, and specify that you are going to 'write' something into the file by ''w'

#f = open('PhilosL_Job/Data/URL_List.txt', 'w')


#for a in archieve_list.find_all('a', href=True):

##specify that you'd like to save the texts in which file. in this case, file = f

#    print('https://listserv.liv.ac.uk/'+ a['href'], file = f)







    
