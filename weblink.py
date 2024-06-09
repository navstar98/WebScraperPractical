from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import undetected_chromedriver as uc
# s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
#setup undetected chromedriver online 
options=uc.ChromeOptions()
options.headless=True
driver=uc.Chrome(executable_path="D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe",options=options)

#navigate
url="https://parlvu.parl.gc.ca/Harmony/en/View/EventListView/20240525/-1"

driver.get(url)

#wait for page to load
driver.implicitly_wait(10)

#find the event titles

titles=[]
video_urls=[]

# try:
td=driver.find_elements(By.CLASS_NAME,"tdEventTitle")

for t in td:
    span=t.find_elements(By.TAG_NAME,"span")
    for s in span:
        title=s.text.strip()
        titles.append(title)

    #using Xpath to find video url
# div_url=driver.find_elements(By.XPATH,"/html/body/form/div[2]/main/div/div/div/div[2]/div[2]/div[1]/a")
# # div_url=driver.find_elements(By.TAG_NAME,"div")
# div_url=driver.find_elements(By.XPATH,"//div[contains(@class, 'divEvent')]/ancestor::tr//a[contains(@href, 'VideoURL')]")


    
# for v in div_url:
#     # vs=v.get_attribute('href')
#     vs=v.text.split()
#     video_urls.append(vs)




# except Exception as e: 
#     print("error occured: {e}")
# finally:
#close the driver
driver.quit()

print(len(titles))
print(len(video_urls))

# Ensure both lists are the same length
# min_length = min(len(titles), len(video_urls))
# titles = titles[:min_length]
# video_urls = video_urls[:min_length]

# df=pd.DataFrame({"Titles":titles, "Video URL": video_urls})
# df.to_csv("weblink1.csv")
