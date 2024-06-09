import requests
from bs4 import BeautifulSoup
import re               #re stands for regular expressions

url='https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')

# data=soup.find_all(string =re.compile('Galaxy'))
data=soup.find_all(string =re.compile('Idea'))
# print(data)
for item in data:
    # print(item.text)
    print(item.text.strip())