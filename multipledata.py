import requests
from bs4 import BeautifulSoup
url='https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
# data=soup.find_all(['h4','p','a'])
# print(data)
# data1=soup.find_all(string="Galaxy Tab 3")
# print(data1)

data=soup.find_all(string =re.compile('Galaxy'))
print(data)