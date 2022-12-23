from bs4 import BeautifulSoup


with open("Legistration_Yuan/LY1_list/LY1_personal_page_3.html") as fp:

    soup = BeautifulSoup(fp, 'html.parser')
    list = soup.find("div", class_="col-sm-8")
    narrow = list.find("ul")
    print(narrow.text)