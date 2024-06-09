from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
# locn of chromedriver
s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")

driver=webdriver.Chrome(service=s)

driver.get("https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_data_extraction.htm")
time.sleep(2)
# for complete screenshot
# driver.save_screenshot("D:/DataScientist/WebScraperPractical/screenshot.png")

# for small or part screenshot
driver.find_element(By.XPATH,"/html/body/main/div/div/div[1]/div[1]/div/img").screenshot("D:/DataScientist/WebScraperPractical/small_screen.png")