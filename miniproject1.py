from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")

driver=webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

search=driver.find_element(By.XPATH,"//html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search.send_keys("House of the Dragons")
search.send_keys(Keys.ENTER)
time.sleep(4)

driver.find_element(By.XPATH,"//html/body/div[5]/div/div[13]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div/div/div/div[1]/div/div/span/a/h3").click()
time.sleep(3)

driver.save_screenshot("D:/DataScientist/WebScraperPractical/miniproject1.png")
# time.sleep(5)
