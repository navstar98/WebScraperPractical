from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import undetected_chromedriver as uc

#setup undetected chromedriver online 
options=uc.ChromeOptions()
options.headless=True
#executable_path= where you download chromedriver
driver=uc.Chrome(executable_path="D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe",options=options)

#navigate
url="https://parlvu.parl.gc.ca/Harmony/en/View/EventListView/20240525/-1"

driver.get(url)

#wait for page to load
driver.implicitly_wait(10)

#find the event titles

titles=[]
try:
    td=driver.find_elements(By.CLASS_NAME,"tdEventTitle")

    for t in td:
        span=t.find_elements(By.TAG_NAME,"span")
        for s in span:
            title=s.text.strip()
            titles.append(title)

except Exception as e: 
    print("error occured: {e}")
finally:
#close the driver
    driver.quit()

# check the array length
print(len(titles))

#to store values into excel sheet or csx
df=pd.DataFrame({"Titles":titles})
df.to_csv("weblink1.csv")
