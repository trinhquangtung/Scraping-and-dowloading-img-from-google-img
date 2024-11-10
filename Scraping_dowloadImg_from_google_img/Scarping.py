
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode if needed
driver = webdriver.Chrome(options=options)

def get_image_urls(url, scroll_pause_time=2):
    driver.get(url)

    # Scroll down the page
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)  # Wait for images to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # Break if no more content to load
            break
        last_height = new_height

    # Parse page content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Collect only image URLs that start with 'https' and don't end with 'fallback_opts=TYPE,SIZE,URL'
    image_urls = [
        img['src'] for img in soup.find_all('img')
        if img.get('src', '').startswith('https://encrypted-tbn0') and not img['src'].endswith('fallback_opts=TYPE,SIZE,URL')
    ]

    return image_urls

# URL of the page
url =""
# Fetch image URLs

image_urls = get_image_urls(url)
for i, img_url in enumerate(image_urls, start=1):
    print(f"'{img_url}',")

# Close the driver
driver.quit()
