# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import time
#
# # Initialize WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode if needed
# driver = webdriver.Chrome(options=options)
#
# def get_image_urls(url, scroll_pause_time=2):
#     driver.get(url)
#
#     # Scroll down the page
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(scroll_pause_time)  # Wait for images to load
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:  # Break if no more content to load
#             break
#         last_height = new_height
#
#     # Parse page content with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     # Collect only image URLs that start with 'https'
#     image_urls = [img['src'] for img in soup.find_all('img') if img.get('src', '').startswith('https://encrypted-tbn0')]
#
#     return image_urls
#
# # URL of the page
# url = "https://www.google.com/search?client=opera-gx&hs=RJy&sca_esv=e02818271ce7f460&q=bò+kho&udm=2&fbs=AEQNm0D7NTKsOqMPi-yhU7bWDsijXeHIssQxQHiKhz3Orm0Szk2q6O3Esev6DIwpyqAb2BgF85BRuPPo79PGgFxkr43-tgC09mLCjuCWnGc7KSn2TXiIJcxdYbqcchfYQ-yk-gDUfNYeLxN2teLX9T6YrYmM3BVJshEeTY38ageVooonO3he4tfroNpeMKuV4SaLLf5wtimwDA03v3NpDwNbLR1LOT5AL75GSBdUoUqHHQd_AfFCcVI&sa=X&ved=2ahUKEwi-pIea472JAxXSklYBHT4yBSoQtKgLegQIFhAB&biw=1661&bih=791&dpr=1.13"
# # Fetch image URLs
# image_urls = get_image_urls(url)
# for i, img_url in enumerate(image_urls, start=1):
#     print(f"'{img_url}',")
#
# # Close the driver
# driver.quit()


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
url = "https://www.google.com/search?client=opera-gx&hs=hzB&sca_esv=81bb0b3d6fdc2d1a&q=Cá+sốt+cà+chua&udm=2&fbs=AEQNm0D7NTKsOqMPi-yhU7bWDsijXeHIssQxQHiKhz3Orm0Szk2q6O3Esev6DIwpyqAb2BgF85BRuPPo79PGgFxkr43-tgC09mLCjuCWnGc7KSn2Tfk8NzZmTtYZjrvI6GV5ySofPj92LXd54Sp_06vdKT2PuwAv57L1mtkNcwdHezXL3Ok_k4jNKW5hL3_JXQeK63u95elp-ny7uQrE57cLx3PQ897PGeofiD-NpMob5Qsj__OMly0&sa=X&ved=2ahUKEwiEzfKMp7-JAxWJSWwGHWUgKD4QtKgLegQIGBAB&biw=1661&bih=791&dpr=1.13"
# Fetch image URLs

image_urls = get_image_urls(url)
for i, img_url in enumerate(image_urls, start=1):
    print(f"'{img_url}',")

# Close the driver
driver.quit()
