import requests
import pandas as pd
from bs4 import BeautifulSoup

# url='https://www.oneindia.com/lok-sabha-elections/?utm_source=OI-EN&utm_medium=Header&utm_campaign=LS-Election'
url='https://ticker.finology.in/'
r=requests.get(url)
# print(r)
soup= BeautifulSoup(r.text,'html.parser')
table= soup.find('table',class_="table table-sm table-hover screenertable")
# print(table)

headers=table.find_all("th")
titles=[]
for i in headers:
    title=i.text.strip()
    titles.append(title)
    
# print(titles)

df=pd.DataFrame(columns=titles)
# print(df)


# part=2
# obtain rows tr data
rows=table.find_all("tr")

for i in rows[1:]:
    data=i.find_all("td")
    # print(data)
    row=[tr.text.strip() for tr in data]
    # print(row)
    l=len(df)
    df.loc[l]=row
    
print(df)
df.to_csv("stock_market.csv")