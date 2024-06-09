from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open('Amazon.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all product names
product_names = [tag.text for tag in soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')]

# Find all product prices
product_prices = [tag.text for tag in soup.find_all('span', class_='a-price-whole')]

# Find all product ratings
# product_ratings = [tag.text for tag in soup.find_all('span', class_='a-icon-alt')]

# Create a DataFrame
data = {
    'Product_Name': product_names,
    'Product_Price': product_prices,
    # 'Ratings': product_ratings
}

df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('amazon_products.xlsx', index=False)

print("Data has been written to amazon_products.xlsx")
