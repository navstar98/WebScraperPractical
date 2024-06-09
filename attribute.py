import requests
from bs4 import BeautifulSoup
web = requests.get('https://webscraper.io/')
soup= BeautifulSoup(web.text,'html.parser')
# print(soup)
# tag = soup.div    #{'class': ['container']}
tag = soup.header
#print(tag.attrs)    #{'role': 'banner', 'class': ['navbar', 'fixed-top', 'navbar-expand-lg', 'navbar-dark', 'navbar-static']}
atb=(tag.attrs)
print(atb['class'])     #['navbar', 'fixed-top', 'navbar-expand-lg', 'navbar-dark', 'navbar-static']

#tag1=soup.div.p
tag1=soup.div.p.string
print(tag1)
    