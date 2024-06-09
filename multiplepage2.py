#multiple page part-2 to get data
import requests
import pandas as pd
from bs4 import BeautifulSoup

Names=[]
Prices=[]
Desc=[]
Reviews=[]

for i in range(1,11):
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=" + str(i)
    r=requests.get(url)
    # print(r)   to check status code 200

    soup=BeautifulSoup(r.text,"html.parser")
    box=soup.find("div",class_="DOjaWF gdgoEp")

    # print(soup)

    names=box.find_all("div",class_="KzDlHZ")
    # print(names)

    for i in names:
        name=i.text.strip()
        Names.append(name)
        
    # print(len(Names))

    prices=box.find_all("div",class_="Nx9bqj _4b5DiR")
    for i in prices:
        price=i.text.strip()
        Prices.append(price)

    # print(len(Prices))

    desc=box.find_all("ul",class_="G4BRas")
    for i in desc:
        des=i.text.strip()
        Desc.append(des)
        
    # print(len(Desc))

    revs=box.find_all("div",class_="XQDdHH")
    for i in revs:
        rev=i.text
        # print("Review:", rev)
        Reviews.append(rev if rev else "No reviews")  #if review is empty

    # print(len(Reviews))

df =pd.DataFrame({"Product Name":Names,"Product Price":Prices,"Product Description":Desc,"Product Reviews":Reviews})
# print(df)
df.to_csv("Flipkart multiple page details.csv",index=False)
