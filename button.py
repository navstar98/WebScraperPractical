#using selenium webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)
#open website
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)

driver.find_element("""/html/body/div/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[2]/button""").click()

