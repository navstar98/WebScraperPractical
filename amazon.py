from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.amazon.in/s?k=laprop&ref=nb_sb_noss")
time.sleep(5)  #wait for page to load

Names=[]
# names=driver.find_element(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
names=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span")
for n in names:
    n1=n.text.strip()
    Names.append(n1)
    print(Names)
time.sleep(5)

df=pd.DataFrame({"Product name":Names})
print(df)


# Price: 
#     <span class="a-price-whole">35,990</span>

# Rating:
#     <span class="a-icon-alt">4.0 out of 5 stars</span>