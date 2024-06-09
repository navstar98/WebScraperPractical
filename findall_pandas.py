import requests
import pandas as pd
from bs4 import BeautifulSoup

url='https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)
soup= BeautifulSoup(r.text,'html.parser')
names= soup.find_all('a',class_='title')
# print(names)

product_name=[]

for i in names:
    name=i.text
    product_name.append(name)
    
print(product_name)
print("")

prices=soup.find_all("h4",class_='price float-end card-title pull-right')
prices_list=[]

for i in prices:
    price=i.text
    prices_list.append(price)
    
print(prices_list)
print("")

desc=soup.find_all('p',class_='description')
desc_list=[]
for i in desc:
    des=i.text
    desc_list.append(des)
    
print(desc_list)
print("")

reviews=soup.find_all('p',class_='review-count float-end')
reviews_list=[]                                     #array used to store review point
for i in reviews:
    rev=i.text
    reviews_list.append(rev)
    
print(reviews_list)


#now for dataframe , we use pandas
df=pd.DataFrame({'Product Name':product_name, "Prices":prices_list, "Description" :desc_list, "Reviews":reviews_list})
print(df)

#now to transfer data to sheets like xls, csv
# df.to_csv('product_details.csv')
df.to_excel('product_details.xlsx',index=False)

