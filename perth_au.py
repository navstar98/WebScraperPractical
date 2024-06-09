import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Function to get the HTML content of a webpage using requests
def get_html_content(url):
    response = requests.get(url)
    return response.text

# Function to scrape data using BeautifulSoup
def scrape_data_with_bs4():
    url = "https://www.yellowpages.com.au/search/listings?clue=Construction+Companies&locationClue=Perth+WA"
    html_content = get_html_content(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    
    companies = []
    for listing in soup.find_all('div', class_='search-contact-card'):
        name = listing.find('h2', class_='listing-name').get_text(strip=True)
        phone = listing.find('a', class_='contact-phone').get_text(strip=True)
        website = listing.find('a', class_='contact-url')
        website = website['href'] if website else None
        location = listing.find('p', class_='listing-address').get_text(strip=True)
        
        companies.append({
            'name': name,
            'phone': phone,
            'website': website,
            'location': location
        })
    
    return companies

# Function to scrape data using Selenium
def scrape_data_with_selenium():
    url = "https://www.yellowpages.com.au/search/listings?clue=Construction+Companies&locationClue=Perth+WA"
    s=Service("D:/DataScientist/WebScraperPractical/chromedriver-win64/chromedriver.exe")
    driver=webdriver.Chrome(service=s)

    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    companies = []
    listings = driver.find_elements(By.CLASS_NAME, 'search-contact-card')
    for listing in listings:
        name = listing.find_element(By.CLASS_NAME, 'listing-name').text.strip()
        phone = listing.find_element(By.CLASS_NAME, 'contact-phone').text.strip()
        website_element = listing.find_elements(By.CLASS_NAME, 'contact-url')
        website = website_element[0].get_attribute('href') if website_element else None
        location = listing.find_element(By.CLASS_NAME, 'listing-address').text.strip()

        companies.append({
            'name': name,
            'phone': phone,
            'website': website,
            'location': location
        })

    driver.quit()
    return companies

# Get data using BeautifulSoup
companies_bs4 = scrape_data_with_bs4()

# Get data using Selenium
companies_selenium = scrape_data_with_selenium()

# Combine both lists (if needed)
all_companies = companies_bs4 + companies_selenium

# Create a pandas DataFrame
df = pd.DataFrame(all_companies)

# Save DataFrame to CSV
df.to_csv('perth.csv', index=False)

print("perth.csv")
