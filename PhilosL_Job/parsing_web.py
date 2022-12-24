#initial setup
import requests
from bs4 import BeautifulSoup
import pandas as pd

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
#for a in archieve_list.find_all('a', href=True):
#    print(a.text)
#    print('https://listserv.liv.ac.uk/'+ a['href'])


###option 2 - print out the URLs and save them in a separate txt file so that we will not need to visit the website to get the URLs when we want to use them to do stuff next time. 

#open a new file in the designited location, and specify that you are going to 'write' something into the file by ''w'

#f = open('PhilosL_Job/Data/URL_List.txt', 'w')


#for a in archieve_list.find_all('a', href=True):

##specify that you'd like to save the texts in which file. in this case, file = f

#    print('https://listserv.liv.ac.uk/'+ a['href'], file = f)


#f = open('PhilosL_Job/Data/URL_List.csv', 'w')

#df = pd.read_csv('PhilosL_Job/Data/URL_List.csv', 'w')
#df = df['Time', 'URL']


#option 3 - save the data to a csv file for future use
philosL_df = pd.DataFrame(columns = ['Time', 'URL'])
Time = []
URL = []

for a in archieve_list.find_all('a', href=True):
    temp_time = a.text
    Time.append(temp_time)
    temp_url = 'https://listserv.liv.ac.uk/'+ a['href']
    URL.append(temp_url)

philosL_df['Time'] = Time
philosL_df['URL'] = URL

philosL_df.to_csv(f'PhilosL_Job/Data/URL_List.csv', index = False)

#note!!! there's a "hide latest messages" stuff at the very beginning. do remember to remove the data save in the second row manumally








    
