import requests
from bs4 import BeautifulSoup
# url='https://www.tutorialsfreak.com'
url='https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')
# print(soup.title)
# print(soup.find('h4',{"class":"fw-600 fs-36 label-color-14"}).string)
# print(soup.find('h4',{"class":"fw-600 fs-36 label-color-14"}))
# p=soup.find('h4',{"class":"fw-600 fs-36 label-color-14"})
# print(p.text)
p1=soup.find_all('h4',class_="price float-end card-title pull-right")
# print(p1)
# print(len(p1))   #21 total

# for i in p1:
#     print(i.text)
    
desc =soup.find_all('p', class_='description card-text')
print(desc)

for j in desc:
    print(j.text)