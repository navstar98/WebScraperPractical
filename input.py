#using selenium webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)
#open website
driver.get("https://www.google.com/")
time.sleep(2)

search=driver.find_elements("""//html/body/ntp-app//div/div[2]/cr-realbox//div/input""")
search.send_keys("wscubetech")
search.send_keys(Keys.ENTER)
