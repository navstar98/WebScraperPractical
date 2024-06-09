import requests
from bs4 import BeautifulSoup
web = requests.get('https://www.facebook.com/')
#web
#soup= BeautifulSoup(web.content,"lxml.parser")
soup= BeautifulSoup(web.text,'lxml')
print(soup)


    