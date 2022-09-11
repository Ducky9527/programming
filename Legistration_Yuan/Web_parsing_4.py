import requests
from bs4 import BeautifulSoup


which = 0

for i in range(7):
    which +=1
    f = open(f'LY_list_{which}.txt', 'w')

    response = requests.get(f"Legistration_Yuan/LY{which}.html")
    soup = BeautifulSoup(response.text, "html.parser")
    list = soup.find("section", class_="con_data")
    name = list.find_all("a")

    for j in range(len(name)):
        print("", file=f)
        print(name[j].text, file=f)

        extract = requests.compat.urljoin(
        f"Legistration_Yuan/LY{which}.html", name[j]["href"])

        open_link = requests.get(extract)
        soup = BeautifulSoup(open_link.text, "html.parser")
        print(extract, file=f)

        print(name[j]["href"])

    f.close()