from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# locn of chromedriver
s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")

driver=webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?sca_esv=64731a106f604e99&sca_upv=1&sxsrf=ADLYWIItoUqi2bTHbXza_61Br2ePExoweQ:1715946640224&q=pandas&tbm=isch&source=lnms&sa=X&ved=2ahUKEwi3ocavz5SGAxX_9jgGHUrPAMMQ0pQJegQIDBAB&biw=1536&bih=695&dpr=1.25")

#height of scroll
height=driver.execute_script("return document.body.scrollHeight")
print(height)
time.sleep(10)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
