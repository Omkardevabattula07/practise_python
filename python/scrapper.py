from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the WebDriver (make sure the path to the driver is correct)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the website
driver.get('https://example.com')

# Wait for the content to load (you might need to add explicit waits)
import time
time.sleep(5)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract data
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# Close the WebDriver
driver.quit()