from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
# used to hide chrome visibility(headless mode)
options=ChromeOptions()
options.add_argument('--headless')
# options.headless=True
options.add_argument('--disable-gpu')
# options.add_argument('headless')

s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s, options=options)
driver.get("https://directory.ntschools.net/#/schools")

# implicit wait
# driver.implicitly_wait(20)

selector="#search-panel-container .nav-link"
# links=driver.find_elements(By.CSS_SELECTOR, selector)

# NOW optional explicit wait,
links=WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

school_name_selector=".school-title h1"
results=[]
# for i in range(len(links))
for i in range(3):
    # print(link.text)
    links=WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
    links[i].click()
    # =driver.find_element(By.CSS_SELECTOR, school_name_selector)
    name_e=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, school_name_selector)))
    # print(name_e.text)
    
    
    details={
        'name':name_e.text,
        'physical_add':driver.find_element(By.XPATH,'//div[text()="Physical Address"]/following-sibling::div').text,
        'postal_add':driver.find_element(By.XPATH,'//div[text()="Postal Address"]/following-sibling::div').text,
        'phone_no':driver.find_element(By.XPATH,'//div[text()="Phone"]/following-sibling::*/a').text,
        
    }
    
    results.append(details)
    driver.back()  #goes one step back in browser history

# print(results)
# time.sleep(10)

with open('ntschools_data1.csv','w', newline='', encoding='utf-8') as f:
    writer=csv.DictWriter(f, fieldnames=['name','physical_add','postal_add','phone_no'])
    writer.writeheader()
    writer.writerows(results)
    
driver.quit()
