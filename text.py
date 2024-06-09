import requests
from bs4 import BeautifulSoup
url="https://www.linkedin.com/"
web=requests.get(url)
soup= BeautifulSoup(web.content,'html.parser')
lines=soup.find_all('p')
for l in lines:
	print(l.text)
#print(type(i.get('src')))