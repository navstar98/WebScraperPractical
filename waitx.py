from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#locn of chromedriver
s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.twitter.com/")
# element=WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[5]/header/div/div/div/div[1]/input")))
element=WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')))
# time.sleep(4)

# search=driver.find_element("//html/body/div[5]/header/div/div/div/div[1]/input")
search=driver.find_element('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
search.send_keys("Navdeep Rana")
search.send_keys(Keys.ENTER)



