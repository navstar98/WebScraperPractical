#using selenium webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)
#open website
driver.get("https://www.wscubetech.com/")

driver.find_element("""/html/body/section[1]/div/div/div[2]/img""")

