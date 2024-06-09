#multiple page part-1 to access only links
import requests
from bs4 import BeautifulSoup

for i in range(2,11):
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(i)
    r=requests.get(url)
    # print(r)   to check status code 200

    soup=BeautifulSoup(r.text,"html.parser")
    # print(soup)

    np=soup.find("a",class_="_9QVEpD").get("href")
    # print(np)
    cnp="https://www.flipkart.com"+np
    print(cnp)