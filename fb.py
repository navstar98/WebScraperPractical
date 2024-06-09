from selenium import webdriver
from bs4 import BeautifulSoup
# Initialize a WebDriver instance (make sure you have the appropriate WebDriver installed)
driver = webdriver.Chrome()

# Load the Facebook homepage
driver.get('https://www.facebook.com/')

# Wait for the page to fully render
driver.implicitly_wait(10)  # Adjust the waiting time as needed

# Extract the HTML content
html = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Print the parsed HTML
print(soup)