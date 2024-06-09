import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.tutorialsfreak.com/"
web=requests.get(url)
print(web)
soup= BeautifulSoup(web.content,'html.parser')
img_tags=soup.find_all('img')
Image=[]
for i in img_tags:
    # img=i.text
    src=i.get('src')
    Image.append(src)
    
    print(Image)
	# print(i.get('src'))
	# # print(i.get('alt'))
	# print(type(i.get('src')))
	# # print(type(i.get('alt')))
 
df=pd.DataFrame({'Iamge URL': Image})
print(df)
 
df.to_csv('img.csv') 
