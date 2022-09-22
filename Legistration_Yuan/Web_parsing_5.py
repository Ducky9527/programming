import pandas as pd
from bs4 import BeautifulSoup
import re




for i in range(7):
    
    with open(f"Legistration_Yuan/LY{i+1}.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        sections = soup.find_all("section")

        for section in sections:
            if "id" in section:
                break

        legislators = section.find_all("div", {"class": "inner"})
        legislators_df = pd.DataFrame(columns = ['name', 'party', 'url'])


        for legislator in legislators:
            name = legislator.find("div", {"class": "legislatorname"}).text
            name = re.sub(r"[\n\t\s]*", "", name)
            personal_page_path = legislator.find("a")["href"]
            party = legislator.find("img")["alt"].rstrip("徽章")
            legislators_df.loc[len(legislators_df.index)] = [name, party, personal_page_path]

        

        legislators_df.to_csv(f"LY_list_{i+1}.csv", index = False)