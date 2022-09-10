from bs4 import BeautifulSoup
import pandas as pd


i = 1
#fin = open(f"Legistration_Yuan/LY2.txt") 
# get file handle
#data = fin.read()


# eval() 是 把括號內的東東當作是python的code讀


which = 0
for i in range(7):
    which +=1
    handle = open(f"Legistration_Yuan/LY{which}.txt")

    f = open(f"Legistration_Yuan/LY{which}.html", "w")
    
    data = handle.read()
    data_decoded = eval(data).decode("UTF-8")
    
    print(data_decoded, file = f)

    f.close()
    
