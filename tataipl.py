import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.iplt20.com/auction"
r=requests.get(url)
# print(r)
# soup=BeautifulSoup(r.content,"html.parser")
soup=BeautifulSoup(r.text,"html.parser")
# print(soup)
table=soup.find("table",class_="ih-td-tab auction-tbl")
# print(table)

header=table.find_all("th")
# print(header)
titles=[]
for i in header:
    title=i.text.strip()
    titles.append(title)

# print(titles)
df=pd.DataFrame(columns=titles)
# print(df)    

#obtain rows tr data
rows=table.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    # print(data)
    row=[tr.text.strip() for tr in data]
    # print(row)
    l=len(df)
    df.loc[l]=row

# print(df)
df.to_csv("ipldat.csv")
