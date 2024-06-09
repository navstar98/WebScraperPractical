from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
#locn of chromedriver
s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/feed/")
time.sleep(4)
search=driver.find_element("//html/body/div[5]/header/div/div/div/div[1]/input")
search.send_keys("Navdeep Rana")
search.send_keys(Keys.ENTER)