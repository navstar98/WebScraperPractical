import requests
from bs4 import BeautifulSoup
web = requests.get('https://www.facebook.com/')
web
soup= BeautifulSoup(web.content,"html.parser")
#print(soup.prettify())
soup.title()
soup.p
#soup.find_all('span')
