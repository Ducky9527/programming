from bs4 import BeautifulSoup
import pandas as pd

# To parse a saved page, in this case Legistration_Yuan/LY{i}.txt

i = 1
fin = open(f"Legistration_Yuan/LY{i}.txt") # get file handle
data = fin.read()
print(f"File input with size {len(data)}")

# These LYx.txts were saved from requests.get(url).content
# and were horribly formatted as python bytes laid out as
# plain string. Uncomment the next line
# print(data[0:200])
# to see the "b'\r\n\r\n..." pattern

# Some magics are needes, see:
# https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
# Yet I am lazy so I will use the dangerous eval() to get it done for now.

data_decoded = eval(data).decode('UTF-8')
print(f"After decoding the length became: {len(data_decoded)}")

soup1 = BeautifulSoup(data_decoded, "html.parser")
sections = soup1.find_all("section")

# The section we want will have an attribute called "id"
# ex: <section id="six-legislatorListBox">...</section>
for section in sections:
    if "id" in section: # We found that section which has an "id" attribute
        break # We break the for loop and variable section will be retain the right section to look into

# Process every <div class="inner"> and push into a pandas.df
legislators = section.find_all("div", {"class": "inner"})
legislators_df = pd.DataFrame(columns = ['name', 'party', 'url'])

for legislator in legislators:
    name = legislator.find("div", {"class": "legislatorname"}).text
    personal_page_path = legislator.find("a")["href"]
    party = legislator.find("img")["alt"].rstrip("徽章") # 右邊砍掉徽章兩字
    #print(f"{name} - {personal_page_path} - {party}")
    # Insert a row of [name, party, url] at the last location of the dataframe (#len(legislators_df.index))
    legislators_df.loc[len(legislators_df.index)] = [name, party, personal_page_path]

print(legislators_df)
    